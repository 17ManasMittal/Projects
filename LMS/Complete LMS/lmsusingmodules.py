import book
import member
import transaction
import report
while(True):
    print("="*80)
    print("\t\t\t------Library Management System------\n")
    print("="*80)
    print("\t\t\t\tEnter your choice\n\t\t\t\t1. Book Details\n\t\t\t\t2. Member Details\n\t\t\t\t\
3. Transaction\n\t\t\t\t4. Report\n\t\t\t\t5. Exit")
    choice=int(input())
    if choice==1:
        while(True):
            print("\t\t\t\tEnter your choice\n\t\t\t\t1. Add Book Details\n\t\t\t\t2. Edit Book Details\n\t\t\t\t\
3. Delete a Book\n\t\t\t\t4. Search a Book\n\t\t\t\t5. Back to Main Menu")
            ch=int(input())
            if ch==1:
               book.book_input()
            elif ch==2:
               book.book_edit()
            elif ch==3:
               book.book_delete()
            elif ch==4:
               book.book_search()
            elif ch==5:
                break
    elif choice==2:
        while(True):
            print("\t\t\t\tEnter your choice\n\t\t\t\t1. Add Member Details\n\t\t\t\t\
2. Edit Member Details\n\t\t\t\t3. Delete a Member\n\t\t\t\t4. Search a Member\n\t\t\t\t5. Back to Main Menu")
            ch=int(input())
            if ch==1:
                member.member_input()
            elif ch==2:
                member.member_edit()
            elif ch==3:
                member.member_delete()
            elif ch==4:
                member.member_search()
            elif ch==5:
                break
    elif choice==3:
        while(True):
            print("\t\t\t\tEnter your choice\n\t\t\t\t1. Issue Book\n\t\t\t\t\
2. Return Book\n\t\t\t\t3. Back to Main Menu")
            ch=int(input())
            if ch==1:
                transaction.book_issue()
            elif ch==2:
                transaction.book_return()
            elif ch==3:
                break
    elif choice==4:
        while(True):
            print("\t\t\t\tEnter your choice\n\t\t\t\t1. Book Details\n\t\t\t\t2. Member Details\n\t\t\t\t\
3. Issue Details\n\t\t\t\t4. Return Details\n\t\t\t\t5. Best reading Book(Chart)\n\t\t\t\t6. Back To Main Menu\n")
            ch=int(input())
            if ch==1:
                report.book_output()
            elif ch==2:
                report.member_output()
            elif ch==3:
                report.issue_output()
            elif ch==4:
                report.return_output()
            elif ch==5:
                report.col_chart()
            elif ch==6:
                break
    elif choice==5:
        break
