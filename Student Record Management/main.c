#include <stdio.h>
#include <stdlib.h>
int n; //declare n as global variable 
struct Node { //declaring the structure of the node
    int data; //declaring the data of the node
  int id;
  float gpa;
  struct Node *prev;
  struct Node *next;
};
struct Node *sorted_head;
struct Node *deleteHead(struct Node *head) {
  // Code to delete head from the dll and return new head(4.2)
  if (head == NULL) {
    // Handle the case where the list is empty.
    return NULL;
  }

  struct Node *newHead = head->next;
  if (newHead != NULL) {
    newHead->prev = NULL;
  }
  free(head); // Free the memory of the old head.
  n--;
  return newHead;
}

struct Node *removeDuplicates(struct Node *head, int id) {
  // Code to delete all occurences of the record id and
  // keep only the oldest record with id=id and return new head(4.3)
  struct Node *p = head;
  int count = 0;
  while (p != NULL) {
    if (p->id == id) {
      count++;
      if (count > 1) {
        n--;
        struct Node *prevNode = p->prev;
        struct Node *nextNode = p->next;

        if (prevNode != NULL) {
          prevNode->next = nextNode;
        }
        if (nextNode != NULL) {
          nextNode->prev = prevNode;
        }
        free(p); // Free the memory of the removed node.
      }
    }
    p = p->next;
  }
  return head;
}
struct Node *reverse(struct Node *head) {
  // Code to reverse and dll return new head(4.4)
  struct Node *p = head, *temp;
  while (p != NULL) {
    head = p;
    temp = p->next;
    p->next = p->prev;
    p->prev = temp;
    p = temp;
  }
  return head;
}

struct Node *rotateByKplaces(struct Node *head, int k) {
  // Code to rotate the dll by k places to the right and return new head(4.5)
  struct Node *p = head, *h1 = head, *temp;
  int count = 0;
  if(n>1){
  while (count < n) {
    count++;
    if (count == n - k) {
      temp = p->next;
      p->next = NULL;
      p = temp;
      continue;
    }
    if (count == n - k + 1) {
      p->prev = NULL;
      head = p;
    }
    if (count == n) {
      p->next = h1;
      h1->prev = p;
    }
    p = p->next;
  }
  }
  return head;
}
struct Node *createSortedList(struct Node *head, int n) {
  // Code to create a new dll sorted by gpa (4.6)
  float gpa[n], temp;
  int id[n], t;
  int i = 0;
  struct Node *p = head;
  while (p != NULL) {
    gpa[i] = p->gpa;
    id[i] = p->id;
    p = p->next;
    i++;
  }
  for (int j = 0; j < n - 1; j++) {
    for (int k = 0; k < n - 1 - j; k++) {
      if (gpa[k] < gpa[k + 1]) {
        temp = gpa[k];
        gpa[k] = gpa[k + 1];
        gpa[k + 1] = temp;
        t = id[k];
        id[k] = id[k + 1];
        id[k + 1] = t;
      }
    }
  }
  struct Node *cur = NULL, *back = NULL;
  for (int i = 0; i < n; i++) {
    cur = (struct Node *)malloc(sizeof(struct Node));
    cur->gpa = gpa[i];
    cur->id = id[i];
    if (i == 0) {
      sorted_head = cur;
      sorted_head->prev = NULL;
    } else {
      back->next = cur;
      cur->prev = back;
    }
    back = cur;
  }
  if (n != 0)
    cur->next = NULL;
  return sorted_head;
}

void main() {
  struct Node *head;

  // code to take n, k, duplicate_id as input
  int k, duplicate_id;
  scanf("%d", &n);
  scanf("%d", &k);
  scanf("%d", &duplicate_id);
  // code to take input n records input and build a dll(4.1)
  struct Node *cur = NULL, *back = NULL;

  for (int i = 1; i <= n; i++) {
    cur = (struct Node *)malloc(sizeof(struct Node));
    scanf("%d %f", &cur->id, &cur->gpa);
    if (i == 1) {
      head = cur;
      head->prev = NULL;
    } else {
      back->next = cur;
      cur->prev = back;
    }
    back = cur;
  }
  if (n != 0)
    cur->next = NULL;
  // ...
  // head updated

  head = deleteHead(head);
  head = removeDuplicates(head, duplicate_id);
  head = reverse(head);
  head = rotateByKplaces(head, k);
  sorted_head = createSortedList(head, n);

  // Do not modify the code below
  struct Node *curr = head;
  struct Node *tail = head;
  // print head
  while (curr != NULL) {
    printf("%d,%.1f->", curr->id, curr->gpa);
    tail = curr;
    curr = curr->next;
  }
  printf("\n");
  // print head in reverse ordre
  while (tail != NULL) {
    printf("%d,%.1f->", tail->id, tail->gpa);
    tail = tail->prev;
  }
  printf("\n");
  curr = sorted_head;
  tail = curr;
  // print sorted_head 
  while (curr != NULL) {
    printf("%d,%.1f->", curr->id, curr->gpa);
    tail = curr;
    curr = curr->next;
  }
  printf("\n");
  // print sorted_head in reverse ordre
  while (tail != NULL) {
    printf("%d,%.1f->", tail->id, tail->gpa);
    tail = tail->prev;
  }
  printf("\n");
}
