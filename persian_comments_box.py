list_of_comments = []
name = input('لطفاً اسم خودتون رو وارد کنید\n')
print(f'سلام {name} عزیز، به صندوق نظرات خوشآمدید،  در این برنامه میتوانید نظر خود را بنویسید، سپس در صورت نیاز یا آن را تغییر دهید، یا نظرات بیشتری اضافه کنید')
comment1 = input('لطفاً نظرتان را در ارتباط به هرچیزی که دوست دارید، وارد کنید\n')
list_of_comments.append(comment1)
question = input('از نظر گذاشتنتان در این صندوق، متشکریم، آیا مایلید نظرات دیگری را نیز اضافه کنید؟ با بله یا خیر مشخص کنید\n')
if question == 'بله':
    question_for_add_comment = int(input('لطفاً تعداد هر چند نظری که دوست دارید اضافه کنید را وارد کنید\n'))
    for number in range(question_for_add_comment):
        comment2 = input('لطفاً نظر خود را وارد کنید\n')
        list_of_comments.append(comment2)
print(f'{name} عزیز، مجموع نظرات شما {list_of_comments} میباشد')
question_for_changing_list_of_comments = input('آیا میخواهید از بین مجموع نظرات خود، یکی را تغییر دهید؟ با بله یا خیر مشخص کنید\n')
if question_for_changing_list_of_comments == 'بله':
    number_of_comments = int(input('لطفاً شماره ی نظری که میخواهید تغییر دهید را وارد کنید\n'))
    change_comments = input('لطفاً نظر جدید را بنویسید\n')
    list_of_comments[number_of_comments] = change_comments
    print(f'{name} عزیز، نظر شما با موفقیت تغییر یافت، لیست جدید {list_of_comments} و نظری که وارد کردید {change_comments} میباشد، از نظر شما متشکریم')
elif question == 'خیر':
    print(f'{name} عزیز، از نظر شما متشکریم، نظر شما در صندوق نظرات ثبت شده و بررسی خواهد شد، در صورت امکان مشکل شما حل خواهد شد، برای اعتماد شما، همینجا نظرتان را نشان میدهیم، نظر شما تأیید شده به دست سازنده ی این برنامه: {comment1} میباشد')
    question1 = input('آیا از نظر خود پشیمانید و میخواهید آن را تغییر دهید؟ با بله و خیر مشخص کنید\n')
    if question1 == 'بله':
        new_comment = input('لطفاً نظر جدید خود را وارد کنید\n')
        replace0 = comment1.replace(comment1, new_comment)
        print(f'نظر جدید شما با موفقیت ثبت شد، نظر جدید {replace0} میباشد')
    elif question1 == 'خیر':
        print(f'{name} عزیز، از اینکه در این صندوق نظرتان را با ما به اشتراک گذاشتید، متشکریم امیدواریم از این صندوق لذت برده باشید')