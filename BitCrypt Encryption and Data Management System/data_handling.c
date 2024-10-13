#include <stdio.h>
#include <string.h>
int nemploy = 0;
struct employee { //define a structure 
  int Employee_ID;
  char First_Name[30];
  char Last_Name[30];
  int salary;
  char Joining_Date[10];
} e[101], temp;

void task1() { //function to add employee details
  nemploy++;
  scanf("%d", &e[nemploy].Employee_ID);
  scanf("%s", e[nemploy].First_Name);
  scanf("%s", e[nemploy].Last_Name);
  scanf("%d", &e[nemploy].salary);
  scanf("%s", e[nemploy].Joining_Date);
}

void task2() { //function to delete employee details
  int id, index;
  scanf("%d", &id);
  for (int i = 1; i <= nemploy; i++) {
    if (id == e[i].Employee_ID) {
      index = i;
      break;
    }
  }
  temp.Employee_ID = e[index].Employee_ID;
  strcpy(temp.First_Name, e[index].First_Name);
  strcpy(temp.Last_Name, e[index].Last_Name);
  temp.salary = e[index].salary;
  strcpy(temp.Joining_Date, e[index].Joining_Date);

  for (int j = index; j < nemploy; j++) {
    e[j].Employee_ID = e[j + 1].Employee_ID;
    strcpy(e[j].First_Name, e[j + 1].First_Name);
    strcpy(e[j].Last_Name, e[j + 1].Last_Name);
    e[j].salary = e[j + 1].salary;
    strcpy(e[j].Joining_Date, e[j + 1].Joining_Date);
  }
  e[nemploy].Employee_ID = temp.Employee_ID;
  strcpy(e[nemploy].First_Name, temp.First_Name);
  strcpy(e[nemploy].Last_Name, temp.Last_Name);
  e[nemploy].salary = temp.salary;
  strcpy(e[nemploy].Joining_Date, temp.Joining_Date);
  nemploy--;
}

void task3() { //function to display employee details
  int id;
  scanf("%d", &id);
  for (int i = 1; i <= nemploy; i++) {
    if (e[i].Employee_ID == id) {
      printf("%d ", e[i].Employee_ID);
      printf("%s ", e[i].First_Name);
      printf("%s ", e[i].Last_Name);
      printf("%d ", e[i].salary);
      printf("%s\n", e[i].Joining_Date);
      break;
    }
  }
}

void task4() { ////function to display details of all employees currently in the system
  int id[nemploy + 1], p, temp;
  for (int i = 1; i <= nemploy; i++) {
    id[i] = e[i].Employee_ID;
  }
  int min = id[1];
  for (int j = 1; j < nemploy; j++) {
    for (int k = j; k <= nemploy; k++) {
      if (id[k] < min) {
        min = id[k];
        p = k;
      }
    }
    if (min != id[j]) {
      temp = id[j];
      id[j] = min;
      id[p] = temp;
    }
    min = id[j + 1];
  }
  for (int k = 1; k <= nemploy; k++) {
    for (int l = 1; l <= nemploy; l++) {
      if (e[l].Employee_ID == id[k]) {
        printf("%d ", e[l].Employee_ID);
        printf("%s ", e[l].First_Name);
        printf("%s ", e[l].Last_Name);
        printf("%d ", e[l].salary);
        printf("%s\n", e[l].Joining_Date);
        break;
      }
    }
  }
}

void task5() { //function to update salary
  int id, salary;
  scanf("%d%d", &id, &salary);
  for (int i = 1; i <= nemploy; i++) {
    if (e[i].Employee_ID == id) {
      e[i].salary = salary;
      break;
    }
  }
}

void task6() { //function to find min, max, and mean salary
  int min, max, sum = 0;
  float mean;

  min = max = e[1].salary;
  for (int i = 1; i <= nemploy; i++) {
    if (e[i].salary > max)
      max = e[i].salary;
    if (e[i].salary < min)
      min = e[i].salary;
    sum += e[i].salary;
  }
  mean = sum / nemploy;
  printf("%d %d %.2f", min, max, mean);
  printf("\n");
}
 
void task7() { //function to find no. of employees present at a given date
  int i, count = 0;
  char date[10], year[5], day[3], month[3], y[5], d[3], m[3];
  scanf("%s", date);
  strncpy(year, date + 6, 4);
  year[4] = '\0';
  strncpy(day, date, 2);
  day[2] = '\0';
  strncpy(month, date + 3, 2);
  month[2] = '\0';
  for (i = 1; i <= nemploy; i++) {
    strncpy(y, e[i].Joining_Date + 6, 4);
    y[4] = '\0';
    strncpy(d, e[i].Joining_Date, 2);
    d[2] = '\0';
    strncpy(m, e[i].Joining_Date + 3, 2);
    m[2] = '\0';
    if (strcmp(y, year) < 0)
      count++;
    else if (strcmp(m, month) < 0 && strcmp(y, year) == 0)
      count++;
    else if (strcmp(d, day) < 0 && strcmp(m, month) == 0 &&
             strcmp(y, year) == 0)
      count++;
  }
  printf("%d", count);
  printf("\n");
}

int main(void) {
  // Write your code here

  int n, t;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &t);
    if (t == 1)
      task1();
    else if (t == 2)
      task2();
    else if (t == 3)
      task3();
    else if (t == 4)
      task4();
    else if (t == 5)
      task5();
    else if (t == 6)
      task6();
    else if (t == 7)
      task7();
  }
}
