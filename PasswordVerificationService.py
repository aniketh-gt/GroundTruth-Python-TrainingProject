#!/usr/bin/env python
# coding: utf-8

# # Password Verification Service

# ## TLDR
# 
# - This service will accept user's configuration from INPUT SERVICE otherwise it will use standard configuration 
# - This service will accept password from password generator service
# - This service also has predefined standards for a password in case user wants default password 
# - At last it will verify passwords using Regular Expressions

# In[ ]:


# this service will give me user configuration
user_constraints = input_service()

# this service will return me the generated password and we will verify the password as per the user's configuration
generated_password = password_generator_service() 


# In[3]:


import re
from collections import Counter

# here we will check user's choice if he chose for default then we will use default verifier
def password_verifier(user_constraints,generated_password):
    choice = user_constraints.get("default_auto_password",True)
    
    password_length = user_constraints.get("length_of_password")
    digits_length = user_constraints.get("length_of_number")
    upper_length = user_constraints.get("length_of_uppercase")
    lower_length = user_constraints.get("length_of_lowercase")
    special_sym_length = user_constraints.get("length_of_special_character")


    is_valid = len(generated_password) >= password_length and len(re.findall('[a-z]', generated_password))==lower_length and len(re.findall('[A-Z]', generated_password))==upper_length and len(re.findall('[0-9]', generated_password))==digits_length and len(re.findall("[@#$%=:?./|~>*()<]", generated_password))==special_sym_length

    if(is_valid):
        print(f'Hola! Your default generated password is : ${generated_password}')
    else :
        print("we are sorry, we are not able to verify the default password")

cnst = {"default_auto_password": False,
 'length_of_password': 16,
 'length_of_uppercase': 5,
 'length_of_lowercase': 3,
 "length_of_number": 2,
 'length_of_special_character': 6}

password_verifier(cnst,"%Er$e4.Pt=#VV<G3")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




