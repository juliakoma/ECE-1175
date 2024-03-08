#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/time.h>
#include <signal.h>

void timer_handler(int signum)
{
	static int counter = 0;
	struct timeval ts;
	
	counter += 1;
	gettimeofday(&ts, NULL);
	printf("%d.%06d: timer expired %d times\n", ts.tv_sec, ts.tv_usec,counter);
}

int main(){
	struct itimerval timer;
	struct sigaction sa;
	
	memset(&sa, 0, sizeof(sa));
	sa.sa_handler = &timer_handler;
	sigaction(SIGVTALRM, &sa, NULL);
	
	timer.it_value.tv_sec = 0;
	timer.it_value.tv_usec = 500000;
	timer.it_interval.tv_sec = 0;
	timer.it_interval.tv_usec = 500000;
	
	setitimer(ITIMER_VIRTUAL, &timer, NULL);

	while (1)
	{

	}
	
	return 0;
}







