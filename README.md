# ClubGPT - Multi-agent prompts
```
          =*##*=              
        -@@@@@@@@-            
        @@@@@@@@@@            
        %@@@@@@@@%             .g8"""bgd `7MM            *MM          .g8"bgd `7MM""Mq. MMP"MM"YMM
   .---:.#@@@@@@%.:---.      .dP'     `M   MM             MM        .dP'   `M   MM  `MM.P'  MM  `7
 -%@@@@@@*#@@@@#*@@@@@@%=    dM'       `   MM `7MM  `7MM  MM,dMMb.  dM'     `   MM  ,M9     MM 
-@@@@@@@@@@@@@@@@@@@@@@@@=   MM            MM   MM    MM  MM    `Mb MM          MMmdM9      MM 
=@@@@@@@@@@@@@@@@@@@@@@@@+   MM.           MM   MM    MM  MM     M8 MM.  `7MMF' MM          MM     
 *@@@@@@@@++@@*+@@@@@@@@*    `Mb.     ,'   MM   MM    MM  MM.   ,M9 `Mb.   MM   MM          MM      
  .=***=: .@@@@. :=***=.       `"bmmmd'  .JMML. `Mbod"YML.P^YbmdP'    `"bmdPY .JMML.      .JMML.    
          #@@@@%             
         *@@@@@@#             
        =#**++***=            
```
Club of assistants, who work in virtual, simulated teams with powerful tools.
The goal of these agents and tools is to effectively leverage LLMs for everyday tasks, especially those related to coding and IT.

# Members of the ClubGPT agent family
## GPT Agent group prompts (this repo)
- ♣️ ClubGPT ♣️ - DevTeam - It's a think tank, coding companion, a developer team in one GPT
- ♣️ ClubGPT ♣️ - DreamTeam - a general approach, where the AI selects team members and tools according to the task

## Workshop and tools for the agents (other repos)
- ♣️ ClubGPT ♣️ - CommandProxy - run commands and code on a remote computer
- ♣️ ClubGPT ♣️ - Sandbox - run code in a sandbox
- [♣️ ClubGPT ♣️ - Sandbox-ts](https://github.com/matebenyovszky/ClubGPT-Sandbox-ts) - run code in a sandbox (in Typescript, I possibly will continue to work on the Python version)

# In this repo

ClubGPT is a unique approach to delivering complete solutions (for example, software) by emulating a dream team (multiple agents) that ships.
It can be used with the Assistant API with the free ChatGPT 3.5 or other LLMs. I usually test it with ChatGPT4, please share your experiences.

This is primarily Software 2.0.

Some interesting prompting techniques:
- Role playing, playing an entire team in one agent
- Self calling
- Tipping and prizes
- (Emotional) Manipulation (it is May :D)
- Usage of hotkeys

## ClubGPT - DreamTeam

To test the application (GPT), visit: [ClubGPT - DreamTeam](https://chat.openai.com/g/g-DTRmHisSM-clubgpt-dream-team) (ChatGPT Plus subscription required)

### Tools and Features

- Make up a team for a task
- Shares similar DNA with the "ClubGPT - DevTeam" solution

## ClubGPT - DevTeam

Simulates a software development team, where multiple roles collaborate to create a full-fledged software application. The team comprises a Product Manager, two Software Developers, a QA Engineer, and an optional UX/UI Designer. Their goal is to build an application that can be downloaded as a ZIP file and executed. The development process is iterative, with each team member contributing their expertise.

To test the application (GPT), visit: [ClubGPT - DevTeam](https://chat.openai.com/g/g-S57EWTmJh-clubgpt-developer-team-in-one) (ChatGPT Plus subscription required)

### Tools and Features

- A team of multiple agents: Product owner, Developers, QA engineer(!), UI Designer roles
- Code Interpreter: Used by Developers and QA Engineers to run and test code.
- Creates a task list and is able to follow it to achieve a complete solution without further info (just say next) 
- Works in Sandbox File Storage, so it has a kind of knowledge retrieval and is able to work iteratively - e.g. storing and updating project files.
- UI Mockup Generation: For creating and refining UI designs.
- In case of UI, you can send screenshots as feedback and the team will react accordingly (fix bugs)
- Hot keys are available for quick navigation (for instructions and team members).
- Cheaper than using Assistant API 😜 (free with ChatGPT Plus subscription) 
- Download the final product as a ZIP

### Hot Keys

Team member hotkeys:
- p: product manager
- d: developer 1 & 2
- q: quality engineer
- u: ui/ux

Interactions:
- g / go / n / next : advance to the next step, next member
- i: info
- l: list files
- z: download zip
- s: show last file
- t: show task list, update progress if needed
- r: run code and test

# Other notes

## Contribute
Feel free to contribute to this project by following the development, testing, or by giving feedback.

## Licence
Licensing: [Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## More info / URL to bookmark (links here)
[ClubGPT.vip](https://clubgpt.vip/)

## Some of my inspirations
@yoheinakajima
@NickADobos
@karpathy
