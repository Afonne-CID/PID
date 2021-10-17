#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>
#include <errno.h>

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
	char *lineptr = NULL;
	size_t n = 0;
	int cnt = 0, status;
	pid_t pid;
	FILE *fp;

	fp = fopen("./pids.txt", "r");
	if (!fp)
	{
		printf("Error opening file.");
		exit(1);
	}

	cnt = getline(&lineptr, &n, fp);
	while (cnt != -1)
	{
		cnt = getline(&lineptr, &n, fp);
		lineptr[n] = '\0';
		strtok(lineptr, " ");
		pid = atoi(strtok(NULL, " "));

		printf("Attemping to kill [pid: %d]...\n", pid);

		status = kill(pid, SIGTERM);
		if (status == -1)
		{
			perror("Kill returned -1");
			printf("\n");
		}
		else
			printf("%d was killed successfully\n\n", pid);

		lineptr = NULL;
		n = 0;
		cnt = getline(&lineptr, &n, fp);
	}
	if (cnt == -1)
	{
		free(lineptr);
		exit(1);
	}

	fclose(fp);
	return (0);
}
