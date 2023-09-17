//#include <string.h>
#include <stdio.h>
#include <inttypes.h>
#include <stdbool.h>
#include <iostream>
#include <string>
#include <math.h>
#include <stdlib.h>

using namespace std;

int x = 0;

uint64_t n = 0;
uint64_t sum_t[26] = {};
uint64_t sum_tt[26] = {};
uint64_t start = 0;
uint64_t ender = 0;
double variance[26] = {};
double average[26] = {};
string cracked_pswd = "";
string temp_pswd = "";
char temp_char = 'a';
double temp_high = 0.0;
double temp = 0.0;
unsigned int temp_index = 0;
bool true_key_found = false;
bool letter_found = true;
int randseed = 0;

bool check_password(const char* pwd)
{
	const char* c = "ogqcvangbaethwryobygdkmfljaidmsaukvydxlgqrghmurznhgxqemyzjeeecaxqyltucxsg";
	while (*pwd == *c && *pwd != '\0' && *c != '\0')
	{
		++pwd; ++c;
	}
	return *pwd == *c && *pwd == '\0';
}

static __inline__ uint64_t rdtsc()
{
	uint32_t hi, lo;
	__asm __volatile__("rdtsc" : "=a"(lo), "=d"(hi));
	return ((uint64_t)lo) | (((uint64_t)hi) << 32);
}

int main() {
	//initializing
	n = 0;
	for (unsigned int k = 0; k < 26; k++) {
		sum_t[k] = 0;
		sum_tt[k] = 0;
	}
	//warm-up
	for (unsigned int i = 0; i < 1000; i++) {
		for (unsigned int j = 0; j < 26; j++) {
			temp_char = (char)(97 + j);
			temp_pswd = cracked_pswd + temp_char;
			check_password(temp_pswd.c_str());
		}
	}
	//main code
	while (!true_key_found) {
		//cin >> x;
		for (unsigned int i = 0; i < 10; i++) {
			//randomize sequence
			randseed = rand() % 26;
			//go through 10 traverses through the alphabet before checking the confidence intervals each time 
			for (unsigned int j = 0; j < 26; j++) {
				temp_char = (char)(97 + ((randseed + j) % 26));
				temp_pswd = cracked_pswd + temp_char;
				start = rdtsc();
				true_key_found = check_password(temp_pswd.c_str());
				ender = rdtsc();
				if (true_key_found) {
					printf("GOTCHA!!!!!!\n");
					cracked_pswd += temp_char;
					break;
				}
				sum_t[((randseed + j) % 26)] += (ender - start);
				sum_tt[((randseed + j) % 26)] += (ender - start) * (ender - start);
				//printf("%s\n", temp_pswd.c_str());
				//printf("%lu\n", (ender - start));
			}
			n++;
			if (true_key_found){break;}//break if true key has been found
		}
		if (true_key_found) { break; }//break if true key has been found
		//otherwise calculate the confidence intervals and check
		//if correct letter found, flush n, sum_t, and sum_tt, then update cracked_pswd
		//otherwise go through 10 iterations again
		for (unsigned int h = 0; h < 26; h++) {
			average[h] = sum_t[h] / n;
			variance[h] = (sum_tt[h] - (n * average[h] * average[h])) / (n - 1);
		}
		for (unsigned int h = 0; h < 26; h++) {
			temp = average[h] - 1.15 * sqrt(variance[h]) / sqrt(n);
			if (temp > temp_high) {
				temp_high = temp;
				temp_char = (char)(97 + h);
				temp_index = h;
			}
		}
		for (unsigned int h = 0; h < 26; h++) {
			temp = average[h] + 1.96 * sqrt(variance[h]) / sqrt(n);
			if (temp >= temp_high && h != temp_index) {
				letter_found = false;//remember to reset;
				//break;
			}
		}
		if (letter_found) {
			//correct letter found
			printf("correct letter found: %c\n", temp_char);
			cracked_pswd += temp_char;
			printf("Part of the correct password is: %s\n", cracked_pswd.c_str());
			n = 0;
			for (unsigned int h = 0; h < 26; h++) {
				average[h] = 0;
				variance[h] = 0;
				sum_t[h] = 0;
				sum_tt[h] = 0;
			}
			letter_found = true;
			temp_high = 0.0;
			temp = 0.0;
			temp_index = 0;
		}
		else {
			letter_found = true;
			temp_high = 0.0;
			temp = 0.0;
			temp_index = 0;
		}

	}
	printf("The correct password is: %s\n", cracked_pswd.c_str());
	return 0;
}