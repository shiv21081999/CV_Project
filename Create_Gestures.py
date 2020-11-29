#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt 
import os


# In[ ]:


directory = "Dataset"


# In[ ]:


print("Enter Text: ", end = "")
char = input()
os.mkdir(os.path.join(directory, char))


# In[ ]:


counter = 0


# In[ ]:


cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    img = cv2.flip(img,1)
    img = cv2.resize(img, (1200,900))
    cv2.rectangle(img, (700, 400), (900, 600), (0,255,0))
    hand = img[400: 600, 700:900, :]
    
    cv2.imshow("live", img)
    cv2.imshow("hand", hand)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('s'):
        counter+=1
        cv2.imwrite(os.path.join(directory, char, char+str(counter)+".jpg"), hand)
        print(counter)
        if counter >= 2500:
            break
cap.release()
cv2.destroyAllWindows()


# In[ ]:



# In[ ]:




