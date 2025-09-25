#include <iostream>
#include <unistd.h>
using namespace std;

int main(void)
{
  pid_t x = fork();
  pid_t y = fork();
  printf("PID: %-5d | x: %-5d | y: %-5d\n", getpid(), x, y);
}

/**
 * PID: 30387 | x: 30388 | y: 30389
 * PID: 30389 | x: 30388 | y: 0
 * PID: 30388 | x: 0     | y: 30390
 * PID: 30390 | x: 0     | y: 0
 */