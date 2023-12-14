#include <iostream>
#include <queue>
#include <random>
#include <string>
#include <thread>
#include <chrono>
#include <ctime>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <algorithm>

#define LOG false
#define IPV6 false
struct PlayerSockInfo
{
    int sock;
    int key;
    // Thêm các thông tin khác của người dùng nếu cần
};
struct PlayerInfo
{
    std::string username;
    int id;
    int score;
};

std::vector<PlayerSockInfo> playerInfos;
std::queue<std::string> logQ;
std::set<int> busyPpl;
std::vector<std::pair<int, int>> players;
bool end = false;
bool lock = false;
int total = 0;
int totalsuccess = 0;
const std::string VERSION = "v3.2.0";
const int PORT = 26104;
std::chrono::time_point<std::chrono::steady_clock> START_TIME;

std::vector<PlayerInfo> readPlayersFromFile(const std::string &filename)
{
    std::vector<PlayerInfo> players;
    std::ifstream file(filename);
    std::string line;

    while (std::getline(file, line))
    {
        std::istringstream iss(line);
        PlayerInfo player;
        iss >> player.username >> player.id >> player.score;
        players.push_back(player);
    }

    return players;
}

void writePlayersToFile(const std::string &filename, const std::vector<PlayerInfo> &players)
{
    std::ofstream file(filename);

    for (const auto &player : players)
    {
        file << player.username << " " << player.id << " " << player.score << "\n";
    }
}

int makeInt(const std::string &num)
{
    try
    {
        return std::stoi(num);
    }
    catch (const std::invalid_argument &e)
    {
        return -1;
    }
}

std::string getTime()
{
    auto sec = std::chrono::duration_cast<std::chrono::seconds>(std::chrono::steady_clock::now() - START_TIME).count();
    int minutes = sec / 60;
    sec %= 60;
    int hours = minutes / 60;
    minutes %= 60;
    int days = hours / 24;
    hours %= 24;
    std::stringstream ss;
    ss << days << " days, " << hours << " hours, " << minutes << " minutes, " << sec << " seconds";
    return ss.str();
}

std::string getIp(bool publicIp)
{
    std::string ip;
    if (publicIp)
    {
        try
        {
            std::string url = "https://api64.ipify.org";
            std::string response;
            std::string command = "curl -s " + url;
            FILE *pipe = popen(command.c_str(), "r");
            if (!pipe)
            {
                throw std::runtime_error("popen() failed!");
            }
            char buffer[128];
            while (fgets(buffer, sizeof(buffer), pipe) != nullptr)
            {
                response += buffer;
            }
            pclose(pipe);
            ip = response;
        }
        catch (const std::exception &e)
        {
            ip = "127.0.0.1";
        }
    }
    else
    {
        int sock = socket(AF_INET, SOCK_DGRAM, 0);
        if (sock == -1)
        {
            ip = "127.0.0.1";
        }
        else
        {
            sockaddr_in loopback;
            std::memset(&loopback, 0, sizeof(loopback));
            loopback.sin_family = AF_INET;
            loopback.sin_addr.s_addr = INADDR_LOOPBACK;
            loopback.sin_port = htons(9);
            if (connect(sock, reinterpret_cast<sockaddr *>(&loopback), sizeof(loopback)) == -1)
            {
                ip = "127.0.0.1";
            }
            else
            {
                sockaddr_in name;
                socklen_t namelen = sizeof(name);
                if (getsockname(sock, reinterpret_cast<sockaddr *>(&name), &namelen) == -1)
                {
                    ip = "127.0.0.1";
                }
                else
                {
                    ip = inet_ntoa(name.sin_addr);
                }
            }
            close(sock);
        }
    }
    return ip;
}

void log(const std::string &data, int key = -1, bool adminput = false)
{
    std::string text;
    if (adminput)
    {
        text = "";
    }
    else if (key == -1)
    {
        text = "SERVER: ";
    }
    else
    {
        text = "Player " + std::to_string(key) + ": ";
    }
    if (!data.empty())
    {
        text += data;
        if (!adminput)
        {
            std::cout << text << std::endl;
        }
        if (LOG)
        {
            std::time_t now = std::time(nullptr);
            std::string time = std::asctime(std::localtime(&now));
            logQ.push(time.substr(0, time.length() - 1) + ": " + text + "\n");
        }
    }
    else
    {
        logQ.push("");
    }
}

int getKeyFromSock(int sock)
{
    for (const auto &playerInfo : playerInfos)
    {
        if (playerInfo.sock == sock)
        {
            return playerInfo.key;
        }
    }
    return -1; // hoặc giá trị khác để biểu thị không tìm thấy
}
// void writePlayersToFile(const std::string& filename, const std::vector<PlayerInfo>& players) {
//     std::ofstream file(filename);

//     for (const auto& player : players) {
//         file << player.username << " " << player.id << " " << player.score << "\n";
//     }
// }
void score(int win, int lose)
{
    int id_win, id_lose;
    id_win = getKeyFromSock(win);
    id_lose = getKeyFromSock(lose);
    std::string filename = "username.txt"; // Thay đổi tên file của bạn
    std::vector<PlayerInfo> players = readPlayersFromFile(filename);
    for (auto &player : players)
    {
        if (player.id == id_win)
        {
            // Cộng điểm cho người thắng
            player.score += 1; // Thay đổi dựa trên yêu cầu của bạn
            break;
        }
    }
    for (auto &player : players)
    {
        if (player.id == id_lose)
        {
            // Thay đổi điểm của người thua dựa trên yêu cầu của bạn
            player.score -= 1; // Giả sử bạn muốn trừ điểm khi thua
            break;
        }
    }

    // Ghi lại thông tin vào file
    writePlayersToFile(filename, players);
}
std::string read(int sock, int timeout = -1)
{
    char buffer[9];
    std::memset(buffer, 0, sizeof(buffer));
    // if (timeout != -1)
    // {
    //     timeval tv;
    //     tv.tv_sec = timeout;
    //     tv.tv_usec = 0;
    //     setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, reinterpret_cast<const char *>(&tv), sizeof(tv));
    // }
    ssize_t bytesRead = recv(sock, buffer, sizeof(buffer) - 1, 0);
    if (bytesRead <= 0)
    {
        return "quit";
    }
    std::cout <<sock<<": "<<buffer << std::endl;
    return std::string(buffer);
}

void write(int sock, const std::string &msg)
{
    std::string buffedmsg = msg + std::string(8 - msg.length(), ' ');
    ssize_t bytesSent = send(sock, buffedmsg.c_str(), buffedmsg.length(), 0);
}
std::string remove_space(std::string string)
{
    string.erase(std::remove(string.begin(), string.end(), ' '), string.end());
    return string;
}
int genKey(std::string username)
{
    std::ifstream file("username.txt");
    std::string line;
    while (std::getline(file, line))
    {
        std::istringstream iss(line);
        std::string stored_username;
        int stored_id;
        iss >> stored_username >> stored_id;
        if (username.compare(stored_username) == 0)
        {
            return stored_id;
        }
    }
    return 0;
}

int getByKey(int key)
{
    for (const auto &player : players)
    {
        if (player.second == key)
        {
            return player.first;
        }
    }
    return -1;
}

void mkBusy(std::initializer_list<int> keys)
{
    for (int key : keys)
    {
        busyPpl.insert(key);
    }
}

void rmBusy(std::initializer_list<int> keys)
{
    for (int key : keys)
    {
        busyPpl.erase(key);
    }
}

bool game(int sock1, int sock2)
{
    while (true)
    {
        std::string msg = read(sock1);
        msg = remove_space(msg);
        write(sock2, msg);
        if (msg.compare("quit") == 0)
        {
            return true;
        }
        else if (msg.compare("draw") == 0 || msg.compare("resign") == 0 || msg.compare("end") == 0 || msg.compare("lose") == 0 || msg.compare("win") == 0)
        {
            if (msg.compare("resign") == 0 )
                score(sock2, sock1); 
            else if (msg.compare("lose") == 0 )
                score(sock1, sock2);
            

            // if (msg.compare("win") == 0)
            //     score(sock2, sock1);
            return false;
        }
    }
}

void player(int sock, int key)
{
    while (true)
    {
        std::string msg = read(sock, 3);
        msg = remove_space(msg);

        if (msg.substr(0, 4).compare("quit") == 0)
        {
            return;
        }
        else if (msg.substr(0, 5).compare("pStat") == 0)
        {
            log("Made request for players Stats.", key);
            std::vector<std::pair<int, int>> latestplayers = players;
            std::set<int> latestbusy = busyPpl;
            if (latestplayers.size() > 0 && latestplayers.size() < 11)
            {
                write(sock, "enum" + std::to_string(latestplayers.size() - 1));
                for (const auto &player : latestplayers)
                {
                    if (player.second != key)
                    {
                        if (latestbusy.find(player.second) != latestbusy.end())
                        {
                            write(sock, std::to_string(player.second) + "b");
                        }
                        else
                        {
                            write(sock, std::to_string(player.second) + "a");
                        }
                    }
                }
            }
        }
        else if (msg.substr(0, 2).compare("rg") == 0)
        {
            log("Made request to play with Player" + msg.substr(2), key);
            int oSock = getByKey(std::stoi(msg.substr(2)));
            if (oSock != -1)
            {
                if (busyPpl.find(std::stoi(msg.substr(2))) == busyPpl.end())
                {
                    mkBusy({key, std::stoi(msg.substr(2))});
                    write(oSock, "gr" + std::to_string(key));
                    write(sock, "msgOk");
                    std::string newMsg = read(sock, 3);
                    newMsg = remove_space(newMsg);
                    if (newMsg.compare("ready") == 0)
                    {
                        log("Player " + std::to_string(key) + " is in a game as white");
                        if (game(sock, oSock))
                        {
                            return;
                        }
                        else
                        {
                            log("Player " + std::to_string(key) + " finished the game");
                        }
                    }
                    else if (newMsg.compare("quit") == 0)
                    {
                        write(oSock, "quit");
                        return;
                    }
                    rmBusy({key});
                }
                else
                {
                    log("Player " + std::to_string(key) + " requested busy player");
                    write(sock, "errPBusy");
                }
            }
            else
            {
                log("Player " + std::to_string(key) + " sent invalid key");
                write(sock, "errKey");
            }
        }
        else if (msg.substr(0, 4).compare("gmOk") == 0)
        {

            log("Accepted Player" + msg.substr(4) + " request", key);
            int oSock = getByKey(std::stoi(msg.substr(4)));
            write(oSock, "start");
            log("Player " + std::to_string(key) + " is in a game as black");
            if (game(sock, oSock))
            {
                return;
            }
            else
            {
                log("Player " + std::to_string(key) + " finished the game");
                rmBusy({key});
            }
        }
        else if (msg.substr(0, 4).compare("gmNo") == 0)
        {
            log("Rejected Player" + msg.substr(4) + " request", key);
            write(getByKey(std::stoi(msg.substr(4))), "nostart");
            rmBusy({key});
        }
    }
}
void logThread()
{
    std::ofstream file("SERVER_LOG.txt", std::ios::app);
    while (true)
    {
        std::this_thread::sleep_for(std::chrono::seconds(1));
        while (!logQ.empty())
        {
            std::string data = logQ.front();
            logQ.pop();
            if (data.empty())
            {
                return;
            }
            else
            {
                file << data;
            }
        }
    }
}

void kickDisconnectedThread()
{
    while (true)
    {
        std::this_thread::sleep_for(std::chrono::seconds(10));
        for (auto it = players.begin(); it != players.end();)
        {
            int sock = it->first;
            int key = it->second;
            char buffer[8];
            std::memset(buffer, '.', sizeof(buffer));
            ssize_t bytesSent = send(sock, buffer, sizeof(buffer), 0);
            if (bytesSent > 0)
            {
                int cntr = 0;
                int diff = 8;
                while (true)
                {
                    cntr++;
                    if (cntr == 8)
                    {
                        bytesSent = 0;
                        break;
                    }
                    if (bytesSent == diff)
                    {
                        break;
                    }
                    diff -= bytesSent;
                    bytesSent = send(sock, buffer, diff, 0);
                }
            }
            if (bytesSent == 0)
            {
                log("Player " + std::to_string(key) + " got disconnected, removing from player list");
                it = players.erase(it);
            }
            else
            {
                ++it;
            }
        }
    }
}

void adminThread()
{
    while (true)
    {
        std::string msg;
        std::getline(std::cin, msg);
        log(msg, -1, true);
        if (msg.compare("report") == 0)
        {
            log(std::to_string(players.size()) + " players are online right now,");
            log(std::to_string(players.size() - busyPpl.size()) + " are active.");
            log(std::to_string(total) + " connections attempted, " + std::to_string(totalsuccess) + " were successful");
            log("Server is running " + std::to_string(std::thread::hardware_concurrency()) + " threads.");
            log("Time elapsed since last reboot: " + getTime());
            if (!players.empty())
            {
                log("LIST OF PLAYERS:");
                for (size_t i = 0; i < players.size(); ++i)
                {
                    if (busyPpl.find(players[i].second) == busyPpl.end())
                    {
                        log(" " + std::to_string(i + 1) + ". Player" + std::to_string(players[i].second) + ", Status: Active");
                    }
                    else
                    {
                        log(" " + std::to_string(i + 1) + ". Player" + std::to_string(players[i].second) + ", Status: Busy");
                    }
                }
            }
        }
        else if (msg == "mypublicip")
        {
            log("Determining public IP, please wait....");
            std::string PUBIP = getIp(true);
            if (PUBIP == "127.0.0.1")
            {
                log("An error occurred while determining IP");
            }
            else
            {
                log("This machine has a public IP address " + PUBIP);
            }
        }
        else if (msg.compare("lock") == 0)
        {
            if (lock)
            {
                log("Already in locked state");
            }
            else
            {
                lock = true;
                log("Locked server, no one can join now.");
            }
        }
        else if (msg.compare("unlock") == 0)
        {
            if (lock)
            {
                lock = false;
                log("Unlocked server, all can join now.");
            }
            else
            {
                log("Already in unlocked state.");
            }
        }
        else if (msg.substr(0, 5).compare("kick") == 0)
        {
            std::istringstream iss(msg.substr(5));
            std::vector<int> keys;
            int key;
            while (iss >> key)
            {
                keys.push_back(key);
            }
            for (int k : keys)
            {
                int sock = getByKey(k);
                if (sock != -1)
                {
                    write(sock, "close");
                    log("Kicking player" + std::to_string(k));
                }
                else
                {
                    log("Player " + std::to_string(k) + " does not exist");
                }
            }
        }
        else if (msg.compare("kickall") == 0)
        {
            log("Attempting to kick everyone.");
            std::vector<std::pair<int, int>> latestplayers = players;
            for (const auto &player : latestplayers)
            {
                write(player.first, "close");
            }
        }
        else if (msg.compare("quit") == 0)
        {
            lock = true;
            log("Attempting to kick everyone.");
            std::vector<std::pair<int, int>> latestplayers = players;
            for (const auto &player : latestplayers)
            {
                write(player.first, "close");
            }
            log("Exiting application - Bye");
            log("");
            end = true;
            if (IPV6)
            {
                int sock = socket(AF_INET6, SOCK_STREAM, 0);
                sockaddr_in6 addr;
                std::memset(&addr, 0, sizeof(addr));
                addr.sin6_family = AF_INET6;
                addr.sin6_port = htons(PORT);
                inet_pton(AF_INET6, "::1", &(addr.sin6_addr));
                connect(sock, reinterpret_cast<sockaddr *>(&addr), sizeof(addr));
                close(sock);
            }
            else
            {
                int sock = socket(AF_INET, SOCK_STREAM, 0);
                sockaddr_in addr;
                std::memset(&addr, 0, sizeof(addr));
                addr.sin_family = AF_INET;
                addr.sin_port = htons(PORT);
                inet_pton(AF_INET, "127.0.0.1", &(addr.sin_addr));
                connect(sock, reinterpret_cast<sockaddr *>(&addr), sizeof(addr));
                close(sock);
            }
            return;
        }
        else
        {
            log("Invalid command entered ('" + msg + "').");
            log("See 'onlinehowto.txt' for help on how to use the commands.");
        }
    }
}

bool checkusername(const std::string &username, const std::string &password)
{
    std::ifstream file("account.txt");
    std::string line;
    while (std::getline(file, line))
    {
        std::istringstream iss(line);
        std::string stored_username, stored_password;
        iss >> stored_username >> stored_password;
        if (username.compare(stored_username) == 0 && password.compare(stored_password) == 0)
        {
            return true;
        }
    }
    return false;
}

void initPlayerThread(int sock)
{
    log("New client is attempting to connect.");
    total++;

    std::string username = read(sock, 3);
    username = remove_space(username);
    if (username.empty())
    {
        log("Error reading username from client.");
        return;
    }
    std::string password = read(sock, 3);
    password = remove_space(password);
    if (password.empty())
    {
        log("Error reading password from client.");
        return;
    }
    // while (!checkusername(username, password))
    // {
    //     write(sock, "notOK");
    //     username = read(sock, 3);
    //     password = read(sock, 3);
    // }

    write(sock, "OK");

    if (read(sock, 3).compare("PyChess") == 0)
    {
        log("Client sent invalid header, closing connection.");
        write(sock, "errVer");
    }
    else if (read(sock, 3).compare(VERSION) == 0)
    {
        log("Client sent invalid version info, closing connection.");
        write(sock, "errVer");
    }
    else if (players.size() >= 10)
    {
        log("Server is busy, closing new connections.");
        write(sock, "errBusy");
    }
    else if (lock)
    {
        log("SERVER: Server is locked, closing connection.");
        write(sock, "errLock");
    }
    else
    {
        totalsuccess++;
        int key = genKey(username);
        playerInfos.push_back({sock, key});
        log("Connection Successful, assigned key - " + std::to_string(key));
        players.push_back({sock, key});
        write(sock, "key" + std::to_string(key));
        player(sock, key);
        write(sock, "close");
        log("Player " + std::to_string(key) + " has Quit");
        players.erase(std::remove_if(players.begin(), players.end(), [sock, key](const std::pair<int, int> &player)
                                     { return player.first == sock && player.second == key; }),
                      players.end());
        rmBusy({key});
    }
    close(sock);
}

int main()
{
    int mainSock;

    log("Starting server with IPv4 (default) configuration.");
    mainSock = socket(AF_INET, SOCK_STREAM, 0);
    if (mainSock == -1)
    {
        perror("Error creating IPv4 socket");
        return 1;
    }

    sockaddr_in addr;
    std::memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(mainSock, reinterpret_cast<sockaddr *>(&addr), sizeof(addr)) == -1)
    {
        perror("Error binding IPv4 socket");
        return 1;
    }

    std::string IP = getIp(false);
    if (IP == "127.0.0.1")
    {
        log("This machine does not appear to be connected to a network.");
        log("With this limitation, you can only serve the clients ");
        log("who are on THIS machine. Use IP address 127.0.0.1");
    }
    else
    {
        log("This machine has a local IP address - " + IP);
        log("USE THIS IP IF THE CLIENT IS ON THE SAME NETWORK.");
    }
    if (listen(mainSock, 16) == -1)
    {
        perror("Error listening for connections");
        return 1;
    }

    log("Successfully Started.");
    log("Accepting connections on port " + std::to_string(PORT));

    std::thread(adminThread).detach();
    std::thread(kickDisconnectedThread).detach();

    if (LOG)
    {
        log("Logging is enabled. Starting to log all output");
        std::thread(logThread).detach();
    }

    while (true)
    {
        int s = accept(mainSock, nullptr, nullptr);
        if (s == -1)
        {
            perror("Error accepting connection");
            return 1;
        }

        if (end)
        {
            break;
        }

        std::thread(initPlayerThread, s).detach();
    }

    close(mainSock);
    return 0;
}
