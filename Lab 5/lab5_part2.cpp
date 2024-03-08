#include <iostream>
#include <fstream>
#include <cstdlib>
#include <unistd.h>
#include <string>

int main()
{
	while(1){
		std::ifstream inputFile;
		inputFile.open("/proc/stat");
		std::string line;
		
		if (inputFile.is_open())
		{
			std::getline (inputFile, line);
			std::string name[4];
			
			int user[4], nice[4], system[4], idle[4], iowait[4], irq[4], softirq[4], steal[4], dummy1[4], dummy2[4];
			
			inputFile >> name[0] >> user[0] >> nice[0] >> system[0] >> idle[0] >> iowait[0] >> irq[0] >> softirq[0] >> steal[0] >> dummy1[0] >> dummy2[0];
			inputFile >> name[1] >> user[1] >> nice[1] >> system[1] >> idle[1] >> iowait[1] >> irq[1] >> softirq[1] >> steal[1] >> dummy1[1] >> dummy2[1];
			inputFile >> name[2] >> user[2] >> nice[2] >> system[2] >> idle[2] >> iowait[2] >> irq[2] >> softirq[2] >> steal[2] >> dummy1[2] >> dummy2[2];
			inputFile >> name[3] >> user[3] >> nice[3] >> system[3] >> idle[3] >> iowait[3] >> irq[3] >> softirq[3] >> steal[3] >> dummy1[3] >> dummy2[3];
			
			inputFile.close();
			
			int t_total1[4], t_usage1[4], t_idle1[4];
			
			for (int i = 0; i < 4; i++){
				t_total1[i] = user[i] + nice[i] + system[i] + idle[i] + iowait[i] + irq[i] + softirq[i] + steal[i];
				t_idle1[i] = idle[i] + iowait[i];
				t_usage1[i] = t_total1[i] - t_idle1[i];
			}
			
			sleep(1);
			
			inputFile.open("/proc/stat");
			std::getline (inputFile, line);
			
			inputFile >> name[0] >> user[0] >> nice[0] >> system[0] >> idle[0] >> iowait[0] >> irq[0] >> softirq[0] >> steal[0] >> dummy1[0] >> dummy2[0];
			inputFile >> name[1] >> user[1] >> nice[1] >> system[1] >> idle[1] >> iowait[1] >> irq[1] >> softirq[1] >> steal[1] >> dummy1[1] >> dummy2[1];
			inputFile >> name[2] >> user[2] >> nice[2] >> system[2] >> idle[2] >> iowait[2] >> irq[2] >> softirq[2] >> steal[2] >> dummy1[2] >> dummy2[2];
			inputFile >> name[3] >> user[3] >> nice[3] >> system[3] >> idle[3] >> iowait[3] >> irq[3] >> softirq[3] >> steal[3] >> dummy1[3] >> dummy2[3];
			
			inputFile.close();
			
			int t_total2[4], t_usage2[4], t_idle2[4];

			for (int i = 0; i < 4; i++){
				t_total2[i] = user[i] + nice[i] + system[i] + idle[i] + iowait[i] + irq[i] + softirq[i] + steal[i];
				t_idle2[i] = idle[i] + iowait[i];
				t_usage2[i] = t_total2[i] - t_idle2[i];
			}
			
			int delta_total[4], delta_usage[4], freq_choice(50), desiredFreq, nextFreq[4];
			float util[4];
			
			// calculating cpu util
			for (int i = 0; i < 4; i++)
			{
				delta_total[i] = t_total2[i] - t_total1[i];
				delta_usage[i] = t_usage2[i] - t_usage1[i];
				util[i] = ((float)delta_usage[i] / (float)delta_total[i])*100;
				std::cout << "CPU" << i << ":" << util[i] << "%" << std::endl;
			}
			
			// max util
			float maxUtil=0;
			
			for (int i = 0; i < 4; i++)
			{
				if (maxUtil < util[i])
				{
					maxUtil = util[i];
				}
			}
			
			std::cout << "max util: " << maxUtil << "%" << std::endl;
			
			// desired frequency
			desiredFreq = 1.25*15000*maxUtil;

			// next frequency options
			int freq_option[4] = {600000, 750000, 1000000, 15000000};
			int index = 0;
			
			for (int i = 0; i < 4; i++)
			{
				nextFreq[i] = desiredFreq / freq_option[i];
				
				if (freq_choice > nextFreq[i])
				{
					freq_choice = nextFreq[i];
					index = i;
				}
			}
			
			std::cout << "next freq: " << desiredFreq << std::endl << std::endl;
			
			std::ofstream outfile;
			outfile.open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed");
			outfile << desiredFreq;
			outfile.close();
		}
		else
		{
			std::cout << "Couldn't open file" << std::endl;
		}
	}
	return 0;
}

