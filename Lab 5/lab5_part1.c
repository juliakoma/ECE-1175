#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(){
	
	int result = 0;
	const long long int interval_time = 500000000;
	
	srand((unsigned)(NULL));
	
	clock_t start_time = clock();
	
	for (long int i = 0; i < interval_time; i++){
		if (result > 1000){
			result -= 1;
		}
		else{
			result += 1;
		}
	}
	
	clock_t end_time = clock();
	
	float elapse = (float)(end_time - start_time)/CLOCKS_PER_SEC;
	
	printf("Exec time: %.4f seconds\n", elapse);
	
	return 0;
	
}

