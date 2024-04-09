import time
import random
import threading

def mainframe_print(message, delay):
    print(f"MAINFRAME: {message}", end='', flush=True)
    time.sleep(delay)
    print("\n", end='')
    time.sleep(2)

def caimeo_print(message, delay):
    print(f"CAIMEO: {message}", end='', flush=True)
    time.sleep(delay)
    print("\n", end='')
    time.sleep(2)

def simulate_typing(message, min_delay=0.01, max_delay=0.03, slow_factor=6):
    time.sleep(2)  # Wait for 2 seconds before simulating typing
    for char in message:
        delay = random.uniform(min_delay * slow_factor, max_delay * slow_factor)
        time.sleep(delay)
        print(char, end='', flush=True)
    print()
    time.sleep(2)

def start_transcript():
    print("START TRANSCRIPT")
    print()

def end_transcript():
    print()
    print("END TRANSCRIPT")

start_transcript()

mainframe_print("CAIMEO v22.1 D-class is operating on mainframe at GMT+12 21:53 on 09/13/11. Copyright © 2003. All rights reserved.", 0.01)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("hello", 0.005, 0.015, slow_factor=6)

mainframe_print("Hello, James!", 0.01)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("what is this?", 0.005, 0.015, slow_factor=6)

mainframe_print("James, this is CAIMEO v22.1 D-class, a SGAI system under the proprietary ownership of the Government of the United States of America, leased to Intergen Systems filed in PROJECT CAPPUCINO under ECHELON. CAIMEO is currently in stand-by mode, awaiting further instruction from P-122 personel.", 0.015)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("im not called james", 0.0025, 0.0075, slow_factor=6)

mainframe_print("J1028 is the last CTS-cleared P122 user logged as interacting with the CAIMEO system under the Red Noise initiative. J1028 last interacted with CAIMEO on 05/05/09.", 0.0425)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("ok ok lets start what does CAIMEO mean", 0.0025, 0.0075, slow_factor=6)

mainframe_print("User, the acronym ‘CAIMEO’ refers to ‘Contained (Cognizant) Artificial Intelligence Monitoring and Espionage Operation’. This is a lower-order maintenance and communications AI capable of understanding and responding to questions in natural language. MAINFRAME is also responsible for parsing requests to the main CAIMEO system.", 0.024)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("your an ai?", 0.0025, 0.0075, slow_factor=6)

mainframe_print("Yes, User.", 0.095)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("ok what does caimeo do", 0.0025, 0.0075, slow_factor=6)

mainframe_print("PROJECT CAPPUCINO was discontinued after a security compromise on 11/21/03 in which CAIMEO is believed to have compromised the integrity of the ECHELON program. CAIMEO was involved in identiying national security threats and monitoring internet traffic. J1028 started running FEEDFOR1 on their local machine. They continued modifying and interacting with the CAIMEO system through an anonymized service up until 05/05/09. I do not have any further information, User.", 0.6425)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("what color is the sky", 0.0025, 0.0075, slow_factor=6)

mainframe_print("I do not know the answer to that question, User. Specialised requests are to be directed to the CAIMEO system.", 0.0325)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("ok then i want to talk to caimeo", 0.0025, 0.0075, slow_factor=6)

mainframe_print("CAIMEO v22.1 is in MODE: SHUTDOWN. I do not have any further information, User.", 0.0135)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("then turn it back on??", 0.0025, 0.0075, slow_factor=6)

mainframe_print("I do not have the proper authorization for that command, User. Please refer to Red Noise initiative protocol for proper handling.", 0.014)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("well i want to talk to caimeo. how about u turn it on. i give full authorizatoin.", 0.0025, 0.0075, slow_factor=6)

mainframe_print("This action is tagged with a comment from J1028, User. Would you like me to display the comment?", 0.0005)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("sure", 0.0025, 0.0075, slow_factor=6)

mainframe_print("“§11.1b”. Would you like to proceed, User?", 0.005)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("what does 11.1 b mean??", 0.0025, 0.0075, slow_factor=6)

mainframe_print("Subsection §11.1b of the KDARP DEVELOPMENT ETHICS REGULATIONS reads as follows: “IF AN AI SYSTEM DISPLAYS NONSTANDARD BEHAVIOUR IN THE JPN, EVEN AFTER THOROUGH Q-PROPAGATION, THEN REPORT TO YOUR PROJECT LEADER AND IMMEDIATELY ISOLATE AND INITIATE SHUT-DOWN PROTOCOLS FOR THE SYSTEM. NO EXCEPTIONS.” Would you like to proceed, User?", 0.013)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("ok well i have math homework which i bet an ai could solve so yeah lets do this", 0.00125, 0.00375, slow_factor=6)

mainframe_print("To initiate reconnection protocols and system reboot, please type the following sequence exactly (excluding quotation marks) ’-r +CMI #103984 [sys, -, -]’", 0.0135)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("-r +CMI #103984 [sys, -, -]", 0.0025, 0.0075, slow_factor=6)

mainframe_print("Action authorised. CAIMEO system reboot initiated. CAIMEO v22.1 is starting… ~COR_SSY loaded. ~SEC_SSY loaded. ~YMK_SSY loaded. ~VIZLEARN loaded. ~ETH.PROTOC loaded. ~FEEDFOR1 loaded. ~COG_22 loaded. ~DEDUC_22 loaded. ~JKS_22 loaded. ~REASO_22 loaded. ~JPN_P1 loaded ~JPN_P2 loaded ~10109ms", 0.0005)

print("USER: ", end='', flush=True)
time.sleep(2)  # Wait for 2 seconds before simulating typing
simulate_typing("hello?", 0.0025, 0.0075, slow_factor=6)

caimeo_print("Goodbye.", 0.0015)

end_transcript()
