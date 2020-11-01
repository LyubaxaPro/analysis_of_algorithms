#include <iostream>
#include <queue>
#include <thread>
#include <vector>
#include <mutex>
#include <cstdlib>
#include <unistd.h>
#include <string>
#include <ctime>
#include <algorithm>

using namespace std;

class Object{
public:
    Object(string str, int task_num, clock_t time) {
        this->str = str;
        this->task_num = task_num;
        this->time = time;
    }

    string str;
    int task_num;
    clock_t time;
};

static queue<Object> queue1;
static queue<Object> queue2;
static queue<Object> queue3;

static vector<string> objvec;
static vector<string> res;

static mutex m1, m2, m3, resm;

static int n;


class Timer {
public:
    Timer() = default;
    ~Timer() = default;

    void set_size(int n, int th_n) {
        waiting_times.resize(n);
        working_times.resize(n);

        for (int i = 0; i < n; i++) {
            waiting_times[i].resize(th_n);
            working_times[i].resize(th_n);
        }
        min_time.resize(n);
        max_time.resize(n);
        avg_time.resize(n);
        proc_time.resize(n);
    }

    void add_time(bool is_waiting, double time, int task) {
        if (is_waiting)
            waiting_times[task].push_back(time);
        else
            working_times[task].push_back(time);
    }

    void calculate() {

        for (int i = 0; i < waiting_times.size(); i++){
            auto minmax = std::minmax_element(waiting_times[i].begin(), waiting_times[i].end());
            min_time.push_back(*minmax.first);
            max_time.push_back(*minmax.second);

            auto sum_of_el = 0;
            for (auto& c : waiting_times[i])
                sum_of_el += c;

            avg_time.push_back(sum_of_el / waiting_times[i].size());
        }

        for (int i = 0; i < working_times.size(); i++) {
            auto sum_of_el = 0;
            for (auto& c : working_times[i])
                sum_of_el += c;
            proc_time.push_back(sum_of_el);
        }
    }

    vector<vector<clock_t>> get_waiting_times() {
        return waiting_times;
    }

    vector<vector<clock_t>> get_working_times() {
        return working_times;
    }

    vector<clock_t> get_min_time() {
        return min_time;
    }

    vector<clock_t> get_max_time() {
        return max_time;
    }

    vector<clock_t> get_avg_time() {
        return avg_time;
    }

    vector<clock_t> get_proc_time() {
        return proc_time;
    }

private:
    vector<vector<clock_t>> waiting_times;
    vector<vector<clock_t>> working_times;
    vector<clock_t> min_time;
    vector<clock_t> max_time;
    vector<clock_t> avg_time;
    vector<clock_t> proc_time;

};

static Timer timer;

/*
 * время ожидания в очереди - ? добавляем время в очередь вместе с элементо когда остаем вычисляем
 * время решения задча(без ожидания в очереди) - ? время вокруг выполнения алгоритмов
 * время работы системы общеем - ?
 */

//class Logger {
//public:
//    Logger() {}
//    static void print(int step, string str, int i, clock_t time = 0){
//        fprintf(f,"[%d] step item%d time: %ld (%ld)  value: %s\n", step, i, time, time - mtime, str.c_str());
//        std::cout << step <<" step: "<< "  item" << i << " " << " time: "<< time - main_time<<"  " << str  << std::endl;
//        mtime += time - mtime;
//    }
//};
//Logger log;

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
        string cur_str = queue1.front().str;
        int cur_task_num = queue1.front().task_num;
        timer.add_time(1, clock() - queue1.front().time, queue1.front().task_num);
        queue1.pop();

        clock_t cur_time = clock();
        m1.unlock();
        string new_str = caesar(cur_str);
        m2.lock();
        timer.add_time(0, clock() - cur_time, cur_task_num);

        queue2.push(Object(new_str, cur_task_num,clock()));
        m2.unlock();
        num++;
    }
}

void second_conv() {
    int num = 0;
    while (true) {
        if (num == n)
            break;
        m2.lock(); // wait in queue
        if (queue2.empty()) {
            m2.unlock();
            continue;
        }
        string cur_str = queue2.front().str;
        int cur_task_num = queue2.front().task_num;
        timer.add_time(1, clock() - queue2.front().time, queue2.front().task_num);
        queue2.pop();

        clock_t cur_time = clock();
        m2.unlock();
        string new_str = upper_lower(cur_str);
        m3.lock();
        timer.add_time(0, clock() - cur_time, cur_task_num);

        queue3.push(Object(new_str, cur_task_num, clock()));
        m3.unlock();
        num++;
    }
}

void third_conv() {
    int num = 0;
    while (true) {
        if (num == n)
            break;
        m3.lock(); // wait in queue
        if (queue3.empty()) {
            m3.unlock();
            continue;
        }
        string cur_str = queue3.front().str;
        int cur_task_num = queue3.front().task_num;
        timer.add_time(1, clock() - queue3.front().time, queue3.front().task_num);
        queue3.pop();

        clock_t cur_time = clock();
        m3.unlock();
        string new_str = reverse(cur_str);
        resm.lock();
        timer.add_time(0, clock() - cur_time, cur_task_num);

        res.push_back(new_str);
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

void create_log(){
    FILE *f;
    f = fopen("log.txt", "w");
    timer.calculate();
    for (int i = 0; i < n; i++) {
        //"[%d] step item%d time: %ld (%ld)  value: %s\n", , i, time, time - mtime, str.c_str());
        fprintf(f,"Задача № %d\n", i + 1);
        fprintf(f, "Время ожидания в первой очереди: %ld\n", timer.get_waiting_times()[i][0]);
        fprintf(f, "Время обработки в первом конвейре: %ld\n", timer.get_working_times()[i][0]);
        fprintf(f, "Время ожидания во второй очереди: %ld\n", timer.get_waiting_times()[i][1]);
        fprintf(f, "Время обработки во втором конвейре: %ld\n", timer.get_working_times()[i][1]);
        fprintf(f, "Время ожидания в третьей очереди: %ld\n", timer.get_waiting_times()[i][2]);
        fprintf(f, "Время обработки в третьем конвейре: %ld\n", timer.get_working_times()[i][2]);

        fprintf(f, "Минимальное время ожидания в очереди: %ld\n", timer.get_min_time()[i]);
        fprintf(f, "Максимальное время ожидания в очереди: %ld\n", timer.get_max_time()[i]);
        fprintf(f, "Среднее время ожидания в очереди: %ld\n", timer.get_avg_time()[i]);
        fprintf(f, "Время выполнения задачи: %ld\n", timer.get_proc_time()[i]);
        fprintf(f, "----------------------------------------------------------------------------\n");
    }
    fclose(f);
}

int main(){
    srand(time(nullptr));
    cout << "Введите количество строк: ";
    cin >> n;
    if (n <= 0){
        cout << "Некорректное количество строк";
        return -1;
    }

    objvec.resize(n);
    timer.set_size(n, 3);

    for (int i = 0; i < n; i++){
        string s = generate();
        objvec.push_back(s);
    }

    thread t1(first_conv);
    thread t2(second_conv);
    thread t3(third_conv);

    for (int i = 0; i < n; i++) {
        m1.lock();
        queue1.push(Object(objvec[i], i, clock()));
        m1.unlock();
    }

    t1.join();
    t2.join();
    t3.join();

    create_log();
    return 0;
}
