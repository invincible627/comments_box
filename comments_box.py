list_of_comments = []
language = input("Select language. Type pe or persian for Persian, and en or english for English\n")
if language.lower() == "n" or language.lower() == "english":
    name = input("Please enter your name\n")
    print(f"Hello dear {name}, welcome to the comments box. In this program, you can write your comment, then if needed, change it, delete it or add more comments.")
    comment1 = input("Please enter your comment about anything you like\n")
    list_of_comments.append(comment1)
    question = input("Thank you for your comment in this box. Would you like to add more comments? Specify with yes, yeah or no, nope\n")
    if question.lower() in ["yes", "yeah"]:
        question_for_add_comment = int(input("Please enter how many comments you would like to add\n"))
        for number in range(question_for_add_comment):
            comment2 = input("Please enter your comment\n")
            list_of_comments.append(comment2)
    print(f"Dear {name}, your total comments are {list_of_comments}")
    question_for_changing_list_of_comments = input("Would you like to change one of your total comments? Specify with yes, yeah or no, nope\n")
    if question_for_changing_list_of_comments.lower() in ["yes", "yeah"]:
        number_of_comments = int(input("Please enter the number of the comment you want to change (starting from 0)\n"))
        change_comments = input("Please write the new comment\n")
        list_of_comments[number_of_comments] = change_comments
        print(f"Dear {name}, your comment has been successfully changed. The new list is {list_of_comments}")
    question_for_delete = input("Would you like to delete one of your comments? Specify with yes, yeah or no, nope\n")
    if question_for_delete.lower() in ["yes", "yeah"]:
        delete_number = int(input("Please enter the number of the comment you want to delete (starting from 0)\n"))
        deleted_comment = list_of_comments.pop(delete_number)
        print(f"Dear {name}, your comment {deleted_comment} has been deleted successfully. New list: {list_of_comments}")
    if question.lower() in ["no", "nope"]:
        print(f"Dear {name}, thank you for your comment. Your comment has been registered and approved: {comment1}")
        question1 = input("Are you regretting your comment and want to change it? Specify with yes, yeah or no, nope\n")
        if question1.lower() in ["yes", "yeah"]:
            new_comment = input("Please enter your new comment\n")
            list_of_comments[0] = new_comment
            print(f"Your new comment has been successfully registered: {new_comment}")
        elif question1.lower() in ["no", "nope"]:
            print(f"Dear {name}, thank you for sharing your comment with us.")
elif language.lower() == "pe" or language.lower() == "persian":
    name = input("لطفاً اسم خودتون رو وارد کنید\n")
    print(f"سلام {name} عزیز، به صندوق نظرات خوشآمدید، در این برنامه میتوانید نظر خود را بنویسید، تغییر دهید، حذف کنید یا نظرات بیشتری اضافه کنید")
    comment1 = input("لطفاً نظرتان را وارد کنید\n")
    list_of_comments.append(comment1)
    question = input("آیا مایلید نظرات بیشتری اضافه کنید؟ با بله یا خیر مشخص کنید\n")
    if question == "بله":
        question_for_add_comment = int(input("تعداد نظراتی که میخواهید اضافه کنید را وارد کنید\n"))
        for number in range(question_for_add_comment):
            comment2 = input("نظر خود را وارد کنید\n")
            list_of_comments.append(comment2)
    print(f"{name} عزیز، مجموع نظرات شما {list_of_comments} میباشد")
    question_for_changing_list_of_comments = input("آیا میخواهید یکی از نظرات را تغییر دهید؟ با بله یا خیر مشخص کنید\n")
    if question_for_changing_list_of_comments == "بله":
        number_of_comments = int(input("شماره نظری که میخواهید تغییر دهید را وارد کنید (از 0 شروع میشود)\n"))
        change_comments = input("نظر جدید را بنویسید\n")
        list_of_comments[number_of_comments] = change_comments
        print(f"نظر شما با موفقیت تغییر یافت، لیست جدید {list_of_comments} میباشد")
    question_for_delete = input("آیا میخواهید یکی از نظرات را حذف کنید؟ با بله یا خیر مشخص کنید\n")
    if question_for_delete == "بله":
        delete_number = int(input("شماره ی نظری که میخواهید حذف کنید را وارد کنید (از 0 شروع میشود)\n"))
        deleted_comment = list_of_comments.pop(delete_number)
        print(f"نظر {deleted_comment} با موفقیت حذف شد، لیست جدید {list_of_comments} میباشد")
    elif question == "خیر":
        print(f"{name} عزیز، نظر شما ثبت و تأیید شد: {comment1}")
        question1 = input("آیا از نظر خود پشیمانید و میخواهید آن را تغییر دهید؟\n")
        if question1 == "بله":
            new_comment = input("نظر جدید را وارد کنید\n")
            list_of_comments[0] = new_comment
            print(f"نظر جدید شما ثبت شد: {new_comment}")
        elif question1 == "خیر":
            print(f"{name} عزیز، از اینکه نظر خود را با ما به اشتراک گذاشتید متشکریم")
else:
    print("invalid language, please restart program again")
    print("زبان وارد شده نادرست است. لطفاً برنامه را دوباره اجرا کنید")