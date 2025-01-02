#pragma once
#define FCFS_FAILURE 10;
#define SJF_FAILURE 11;
#define LJF_FAILURE 12;
#define PRI_SCHED_FAILURE 13;
#define RD_ROB_FAILURE 14;
#define MLQ_FAILURE 15;

int fcfs();
int sjf();
int ljf();
int pri_sched();
int rd_rob();
int mlq();
