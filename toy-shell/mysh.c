#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <dirent.h>
#define MAX 512
#define MVUP100 printf("\033[%dA", 100) 

int isCMD(char *cmd, char *real){
	for(int i = 0; i < strlen(real); i++)
		if(cmd[i] != real[i]) return 0;
	return 1;
}

int ifexist(char *f){
	FILE *file = fopen(f,"r"); 
	if(file = NULL) return 0; 
	else fclose(file); 
	return 1;
}

int main(){
	char cmd[MAX];
	for(int i = 0; i < 100; i++) printf("\n");
	MVUP100;
	while(1){
		printf("mysh > ");
		fgets(cmd, MAX, stdin);
		
		if(!strcmp(cmd, "pwd\n")){
			char cdir[MAX];
    	getcwd(cdir, sizeof(cdir));
    	printf("%s\n", cdir);
		}
		else if(isCMD(cmd, "cd")){
			char cd[MAX];
			int j = 0;
			for(int i = 3, start = 0; i < strlen(cmd)-1; i++){
				if(cmd[i] != ' ') start = 1;
				if(start == 1){
					cd[j] = cmd[i];
					j++;
				}
			}
			cd[j] = '\0';
			
			char cdir[MAX];
    	getcwd(cdir, sizeof(cdir));
    	
			if(strlen(cmd) == 3) chdir(getenv("HOME"));
			else if(cd == ".."){
				chdir("..");
			}else{
				chdir(strcat(strcat(cdir, "/"), cd));
			}
		}
		else if(!strcmp(cmd, "show-dirs\n")){
			char cdir[MAX];
    	getcwd(cdir, sizeof(cdir));
			DIR *dir;
		  struct dirent *ptr;
		  dir = opendir(cdir);
		  while((ptr = readdir(dir)) != NULL){
				struct stat st;
				stat(ptr->d_name, &st);
				if (S_ISDIR(st.st_mode))
					printf("%s\n", ptr->d_name);
		  }
		  closedir(dir);
		}
		else if(!strcmp(cmd, "show-files\n")){
			char cdir[MAX];
    	getcwd(cdir, sizeof(cdir));
			DIR *dir;
		  struct dirent *ptr;
		  dir = opendir(cdir);
		  while((ptr = readdir(dir)) != NULL){
				struct stat st;
				stat(ptr->d_name, &st);
				if (S_ISREG(st.st_mode))
					printf("%s\n", ptr->d_name);
		  }
		  closedir(dir);
		}
		else if(isCMD(cmd, "mkdir")){
			char ndir[MAX];
			int j = 0;
			for(int i = 6; i < strlen(cmd)-1; i++){
				if(cmd[i] != ' '){
					ndir[j] = cmd[i];
					j++;
				}
			}
			ndir[j] = '\0';
			if(mkdir(ndir, S_IRWXU) == -1)
				fprintf(stderr, "%s already exists.\n", ndir);
		}
		else if(isCMD(cmd, "touch")){
			char file[MAX];
			int j = 0;
			for(int i = 6; i < strlen(cmd)-1; i++){
				if(cmd[i] != ' '){
					file[j] = cmd[i];
					j++;
				}		
			}
			file[j] = '\0';
			open(file, O_CREAT, S_IRWXU);
		}
		else if(!strcmp(cmd, "clear\n")){
			for(int i = 0; i < 100; i++) printf("\n");
			MVUP100;
		}
		else if(!strcmp(cmd, "exit\n")){
			break; 
		}
	}
	
	return 1;
}
