#include <iostream>
#include <queue>
#include <thread>
#include <vector>
#include <mutex>
#include <cstdlib>
#include <unistd.h>
#include <string>
#include <ctime>

using namespace std;

static queue<string> queue1;
static queue<string> queue2;
static queue<string> queue3;

static vector<string> objvec;
static vector<string> res;

static mutex m1, m2, m3, resm;

static int n;

FILE *f;

static clock_t main_time = clock();

static clock_t mtime = clock();

class Timer {
  vector<vector<double>> waiting_times;
  vector<vector<double>> working_times;

  void add_time(bool is_waiting, double time, int thread_) {
      waiting_times[thread_].push_back(time);
  }

  void calculate() {}



};

/*
 * время ожидания в очереди - ? добавляем время в очередь вместе с элементо когда остаем вычисляем
 * время решения задча(без ожидания в очереди) - ? время вокруг выполнения алгоритмов
 * время работы системы общеем - ?
 */

class Logger {
public:
    Logger() {}
    static void print(int step, string str, int i, clock_t time = 0){
        fprintf(f,"[%d] step item%d time: %ld (%ld)  value: %s\n", step, i, time, time - mtime, str.c_str());
        std::cout << step <<" step: "<< "  item" << i << " " << " time: "<< time - main_time<<"  " << str  << std::endl;
        mtime += time - mtime;
    }
};
Logger log;

// сдвиг на следующую букву алфавита
string caesar(string s) {
    for(int i = 0 ; i < s.length(); i++){
        if (s[i] == 'z') s[i] = 'a';
        else if (s[i] == 'Z') s[i] = 'A';
        else s[i]++;
    }
    return s;
}


string upper_lower(string s) {
    for(int i = 0; i < s.length(); i++){
        if (islower(s[i])) s[i] = toupper(s[i]);
        else s[i] = tolower(s[i]);
    }
    return s;
}

string reverse(string s) {
    int shift = s.length() / 2;
    for (int i = 0; i < s.length() / 2; i++){
        char st = s[i];
        s[i] = s[i + shift];
        s[i + shift] = st;
//        std::swap
    }
    return s;
}

void first_conv() {
    int num = 0;
    while (true) {
        if (num == n)
            break;
        m1.lock(); // wait in queue
        if (queue1.empty()) {
            m1.unlock();
            continue;
        }
        string cur_str = queue1.front();
        queue1.pop();
        m1.unlock();
        string new_str = caesar(cur_str);
        m2.lock();
        queue2.push(new_str);
        clock_t time = clock();
        Logger::print(1, new_str, num, time);
        m2.unlock();
        num++;
    }
}

void second_conv() {
    int num = 0;
    while (true) {
        if (num == n)
            break;
        m2.lock();
        if (queue2.empty()) {
            m2.unlock();
            continue;
        }
        string my_str = queue2.front();
        queue2.pop();
        m2.unlock();
        string new_str = upper_lower(my_str);
        m3.lock();
        queue3.push(new_str);
        clock_t time = clock();
        Logger::print(2, new_str, num, time);
        m3.unlock();

        num++;
    }
}

void third_conv() {
    int num = 0;
    while (true) {
        if (num == n)
            break;
        m3.lock();
        if (queue3.empty()) {
            m3.unlock();
            continue;
        }
        string my_str = queue3.front();
        queue3.pop();
        m3.unlock();
        string new_str = reverse(my_str);
        resm.lock();
        res.push_back(new_str);
        clock_t time = clock();
        Logger::print(3, new_str, num, time);
        resm.unlock();
        num++;
    }
}

// Диапазон чисел: [min, max]
int get_random_number(int min, int max)
{
    // Установить генератор случайных чисел

    // Получить случайное число - формула
    int num = min + rand() % (max - min + 1);

    return num;
}

string generate() {
    string s = "";
    int reg = 0;
    int code = 0;
    int min_low = 97;
    int max_low = 122;
    int min_upper = 65;
    int max_upper = 90;
    for (int i = 0; i < 500; i++){
        reg = get_random_number(0, 1);
        if (reg) code = get_random_number(min_upper, max_upper);
        else code = get_random_number(min_low, max_low);
        s.push_back(code);
    }
    return s;
}

int main(){
    srand(time(nullptr));
    f = fopen("log.txt", "w");
    cout << "Введите количество строк: ";
    cin >> n;
    if (n <= 0){
        cout << "Некорректное количество строк";
        return -1;
    }

    objvec.resize(n);
    for (int i = 0; i < n; i++){
        string s = generate();
        objvec.push_back(s);
        cout << s << '\n';
    }

    thread t1(first_conv);
    thread t2(second_conv);
    thread t3(third_conv);

    main_time = clock();



    for (int i = 0; i < n; i++) {
        clock_t time = clock();
        Logger::print(0, objvec[i], i, time);
        m1.lock();
        queue1.push(objvec[i]);
        m1.unlock();
        sleep(2);
    }

    t1.join();
    t2.join();
    t3.join();
    fclose(f);
    return 0;
}