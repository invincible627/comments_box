list_of_comments = []
name = input('Please enter your name\n')
print(f'Hello dear {name}, welcome to the comments box. In this program, you can write your comment, then if needed, change it or add more comments.')
comment1 = input('Please enter your comment about anything you like\n')
list_of_comments.append(comment1)
question = input('Thank you for your comment in this box. Would you like to add more comments? Specify with yes, yeah or no, nope\n')

if question.lower() in ['yes', 'yeah']:
    question_for_add_comment = int(input('Please enter how many comments you would like to add\n'))
    for number in range(question_for_add_comment):
        comment2 = input('Please enter your comment\n')
        list_of_comments.append(comment2)
print(f'Dear {name}, your total comments are {list_of_comments}')
question_for_changing_list_of_comments = input('Would you like to change one of your total comments? Specify with yes, yeah or no, nope\n')

if question_for_changing_list_of_comments.lower() in ['yes', 'yeah']:
    number_of_comments = int(input('Please enter the number of the comment you want to change (starting from 0)\n'))
    change_comments = input('Please write the new comment\n')
    list_of_comments[number_of_comments] = change_comments
    print(f'Dear {name}, your comment has been successfully changed. The new list is {list_of_comments} and the comment you entered is {change_comments}. Thank you for your comment.')

if question.lower() in ['no', 'nope']:
    print(f'Dear {name}, thank you for your comment. Your comment has been registered in the comments box and will be reviewed. If possible, your issue will be resolved. For your trust, we show your comment here. Your comment has been approved by the creator of this program: {comment1}')
    question1 = input('Are you regretting your comment and want to change it? Specify with yes, yeah or no, nope\n')
    if question1.lower() in ['yes', 'yeah']:
        new_comment = input('Please enter your new comment\n')
        list_of_comments = new_comment  # Assuming changing the first comment
        print(f'Your new comment has been successfully registered. The new comment is {new_comment}')
    elif question1.lower() in ['no', 'nope']:
        print(f'Dear {name}, thank you for sharing your comment with us in this box. We hope you enjoyed this comments box.')