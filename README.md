# **recalculate_tcp is a tool importing modifying and exporting tooldata for robots. Currently only ABB format supported.**
  
  ![startupScreen](https://github.com/user-attachments/assets/c412e43f-3482-4806-9a9a-27357279f35b)  

Required dependencies:
    Python 3: https://www.python.org/downloads/  
    Numpy: Once python is installed, in your terminal or comand prompt type  
          ```
          pip install numpy
          ```  
    Launch by double clicking recalculate_tcp.py, or typing in a terminal:  
    ```
    python recalculate_tcp
    ``` 

## **Features:**  
### Load from file will parse any txt file or config and find tooldata strings  
### if multipule tools are found you will be prompted to select one:  
    
![multiToolListbox](https://github.com/user-attachments/assets/f1e50a89-289e-43b4-b6bf-84c454b66bb8)  
### Save to new file, and save to file will append the tooldata string to a txt file:  
![toolsToFile](https://github.com/user-attachments/assets/9cd3d3ad-67e6-44c3-a79c-f123225065f4)  
### Load from file will work with these custom outputed txt files:  
![loadFromUserFile](https://github.com/user-attachments/assets/2ea51bfa-393b-4cde-a05d-dd595d7b2e45)  
### You can modify a tool tcp by setting how much it has shifted in mm in the displacement values, and pressing calculate  
### Example output:  
![resultsScreen](https://github.com/user-attachments/assets/c3ccf45a-059f-45fc-ac1b-187d58562da1)




