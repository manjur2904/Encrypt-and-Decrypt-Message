from tkinter import messagebox, simpledialog, Tk

def get_task():
    task = simpledialog.askstring('Task', 'Do want to encrypt or decrypt? \t\t\t')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: \t\t\t')
    return message

def get_even_letters(message):
    even_letters = []
    for i in range(0, len(message)):
        if i % 2 == 0:
            even_letters.append(message[i])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for i in range(0, len(message)):
        if i % 2 == 1:
            odd_letters.append(message[i])
    return odd_letters

def swap_letter(message):
    letter_list = []
    flag = False
    if len(message) % 2 == 1:
        flag = True
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    if flag == False:
        for i in range(0, int(len(message)/2)):
            letter_list.append(odd_letters[i])
            letter_list.append(even_letters[i])
    else:
        for i in range(0, int(len(message)/2)):
            letter_list.append(odd_letters[i])
            letter_list.append(even_letters[i])
        letter_list.append(even_letters[len(even_letters)-1])
    # To covert char array in a string
    new_message = ''.join(letter_list)
    return new_message
    

root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letter(message)
        messagebox.showinfo('Ciphertext of the secret meaasge is: \t\t\t', encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letter(message)
        messagebox.showinfo('Plaintext of the secret meaasge is: \t\t\t', decrypted)

    else:
        break

root.mainloop()