#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map>

using namespace std;

int main(int argc, char *argv[]) {
  string line, one;
  unordered_map<string, int> counter;
  if (argc > 1) { 
    cout << argv[1] << endl;
    ifstream ifs(argv[1]); 
    if (!ifs) { cout << "file not found" << endl; }
    else {
      while (getline(ifs, line, '\n')) {
        stringstream ss_line(line);
        while (getline(ss_line, one, ' ')) {
          counter[one] += 1;
        }
      }
    }
    for (auto itr = counter.begin(); itr != counter.end(); itr++) {
      cout << itr->first << ": " << itr->second << endl;
    }
    cout << "word differencies: " << counter.size() << endl;
    {
  }
}


