import random

class Customer:
    def __init__(self , id , interarrival , times_service):
        self.id = id
        self.interarrival = interarrival
        self.times_service = times_service

        self.arrival_time = 0
        self.start_time = 0
        self.waiting_time = 0
        self.end_time = 0
class QuSimula:
    def __init__(self, num_cust):
        self.num_cust=num_cust
        self.customers = []

    def geninterarrival(self):
        return random.randint(1,8)
    
    def genService_time(self):
        P = random.random()

        if P < 0.1:
            return 1
        elif P < 0.3:
            return 2
        elif P < 0.6:
            return 3
        elif P < 0.85:
            return 4
        elif P < 0.95:
            return 5
        else:
            return 6
        
    def gen_Customers(self):
        for i in range(self.num_cust):
            inter = 0 if i == 0 else self.geninterarrival()
            service = self.genService_time()

            cust = Customer(i+1 ,inter , service)
            self.customers.append(cust)



    def run_sumlation(self):
        for i,c  in enumerate(self.customers):
            if i == 0:
                c.arrival_time = 0
            else:
                c.arrival_time = self.customers[i-1].arrival_time + c.interarrival
            
            if i == 0:
                c.start_time = c.arrival_time
            else:
                c.start_time = max(c.arrival_time , self.customers[i-1].end_time)


            c.waiting_time = c.waiting_time = c.start_time - c.arrival_time


            c.end_time = c.start_time + c.times_service
    
    def statistics(self):
        n = self.num_cust

        total_wait = sum(c.waiting_time for c in self.customers)
        avg_wait = total_wait / n

        
        num_wait = sum(1 for c in self.customers if c.waiting_time > 0)
        prob_wait = num_wait / n

        
        idle_time = 0
        for i, c in enumerate(self.customers):
            if i == 0:
                idle_time += c.start_time  
            else:
                idle_time += max(0, c.arrival_time - self.customers[i-1].end_time)

        total_time = self.customers[-1].end_time
        prob_idle = idle_time / total_time

        
        total_service = sum(c.times_service for c in self.customers)
        avg_service = total_service / n

        
        total_interarrival = sum(c.interarrival for c in self.customers[1:])
        avg_interarrival = total_interarrival / (n - 1)

        
        avg_wait_who_wait = total_wait / num_wait if num_wait > 0 else 0

        
        total_system_time = sum((c.end_time - c.arrival_time) for c in self.customers)
        avg_system_time = total_system_time / n

        
        print("Average Waiting Time:", avg_wait)
        print("Probability of Waiting:", prob_wait)
        print("Probability of Server Idle:", prob_idle)
        print("Average Service Time:", avg_service)
        print("Average Time Between Arrivals:", avg_interarrival)
        print("Average Waiting (who waited):", avg_wait_who_wait)
        print("Average Time in System:", avg_system_time)



sim = QuSimula(20)
sim.gen_Customers()
sim.run_sumlation()
sim.statistics()






