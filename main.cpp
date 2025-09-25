#include <iostream>
#include <unistd.h>
using namespace std;

int main(void)
{
  pid_t x = fork();
  pid_t y = fork();
  printf("PID: %-5d | x: %-5d | y: %-5d\n", getpid(), x, y);
}