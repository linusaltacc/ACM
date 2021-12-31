from re import I
import streamlit as st
from gmail import *
import gmail
import contacts
from contacts import *
user_id = 'me' # change 'me' with email address for commercial use.
gmail_service = gmail.get_service()
contacts_service = contacts.get_service()
def output_data(function):
    i = 1
    for _ in function:
        st.write("Email ", i)
        i += 1
        st.write(_)
        st.write("***")

def output_contacts(all_senders_data):
    total_contacts,i = len(all_senders_data),1
    for sender_data in all_senders_data:
        st.write("From Email ", i)
        # st.write('Name : ', sender_data['sender_name'])
        # st.write('Phone Number : ',sender_data['sender_phone_numbers'])
        # st.write('Email : ',sender_data['sender_email'])
        # st.write('Website : ', sender_data['url'])
        st.button('',key=str(i),on_click=edit_add_contacts(sender_details=[sender_data['sender_name'],sender_data['sender_phone_numbers'],sender_data['sender_email'],sender_data['url']],key=i))
        i += 1
        st.write("***")

def edit_add_contacts(sender_details,key):
    with st.form(key=str(key)):
        name = st.text_input("Name",sender_details[0])
        phone = st.text_input("Phone Number",sender_details[1][0])
        email = st.text_input("Email",sender_details[2])
        url = st.text_input("Website",sender_details[3])

        submit_button = st.form_submit_button(label='Add Contacts')
    if submit_button:
        create_contacts(contacts_service,[name,phone,email,url])
        st.success('Contact Has Been Created!')

def check_option():
    option = st.selectbox(
     'Select Function',
     ('Select a Function','Get All Emails', 'Get All Senders Data','Show Retrived Contacts'))
    if option == 'Get All Emails':
        output_data(get_all_emails(gmail_service,user_id))
    elif option == 'Get All Senders Data':
        output_data(get_all_senders_data(gmail_service,user_id))
    elif option == 'Show Retrived Contacts':
        output_contacts(get_all_senders_data(gmail_service,user_id))

check_option()

