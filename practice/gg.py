import simpy #importing the simpy library
print("SimPy is working!") # just to check

def part(env, name, m1, m2, m3): #  we are defining the 'part' function, and being called at the same time, that has 3 parameters. If you have " name" with the appostrophy, then you already defined the value there, so, it is a error, since, env is not defined before that

    print(f"{name} arrives at time {env.now} to the first stand") # The env(variable) is already defined as the environment "env = simpy.Environment()", and now is the attribute inside the envirenment
    # env is the clock. env.now is what the clock currently shows.
    with m1.request() as req: # wait for the machine to be free (Basically, the process requesting for the usage of the machine) // Gives the request a name 'req'
        yield req # pauses the process untill the request is granted (since the machine is busy), after 'yield req' line, the process occupys the machine
        print(f"{name} starts processing at time {env.now} at M1") #the part occupys the machine, and the code displays at what time, the part is being started operated 
        yield env.timeout(3) # the process for 1 component takes time 3 
        print(f"{name} finishes at time {env.now} at M1") # reflects that tyhe part will finish after the time 3 respectively
        
    with m2.request() as req: # wait for the machine to be free (Basically, the process requesting for the usage of the machine) // Gives the request a name 'req'
        yield req # pauses the process untill the request is granted (since the machine is busy), after 'yield req' line, the process occupys the machine
        print(f"{name} starts processing at time {env.now} at M2") #the part occupys the machine, and the code displays at what time, the part is being started operated 
        yield env.timeout(4) # the process for 1 component takes time 3 
        print(f"{name} finishes at time {env.now} at M2") # reflects that tyhe part will finish after the time 3 respectively

    with m3.request() as req: # wait for the machine to be free (Basically, the process requesting for the usage of the machine) // Gives the request a name 'req'
        yield req # pauses the process untill the request is granted (since the machine is busy), after 'yield req' line, the process occupys the machine
        print(f"{name} starts processing at time {env.now} at M3") #the part occupys the machine, and the code displays at what time, the part is being started operated 
        yield env.timeout(5) # the process for 1 component takes time 3 
        print(f"{name} finishes at time {env.now} at M3") # reflects that tyhe part will finish after the time 3 respectively

def part_arrival(env, m1, m2, m3): # now about the arrival of the part, at what time the part will arrive, with the 2 inputs
    for i in range(20): # 20 parts are there 
        env.process(part(env, f"Part {i+1}", m1, m2, m3)) # one after the other (just for the arrival, that comes after every 4 secounds of previous part arrival)
        yield env.timeout(3)

env = simpy.Environment()
m1 = simpy.Resource(env, capacity=1) # A machine that can process one part at a time
m2 = simpy.Resource(env, capacity=1)
m3 = simpy.Resource(env, capacity=1)
env.process(part_arrival(env, m1, m2, m3)) # Simpy takes the generator (par_arrival(env, machines), and puts it in the simulation envirenment (env.process))
env.run(until=20) # writes the output until time 30, doesnt matter, if the parts are more (since here, 20)
# also now practise the machines or the sations for 3 number ( Location planning)