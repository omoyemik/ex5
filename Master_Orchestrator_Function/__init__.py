import logging
import json
import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    #run locally 
    #input = []
    #for i in range(1,5):
    # filename = f'mrinput-{i}.txt'
     #myfile = open(filename,'r')
    #data = myfile.read()
    #input += data.replace('\r', '').split("\n")
    #print(input[i])
     #   myfile.close()

    #download from blob storage
    input = yield context.call_activity('GetInputDataFn')

    tasks = []
    for line in input:
        tasks.append(context.call_activity("Mapper_Activity_Function", line))
    mpp = yield context.task_all(tasks)
    
    flat_mpp = [item for sub in mpp for item in sub]

    shff = yield context.call_activity('Shuffler_Activity_Functions', flat_mpp)
    
    tasks = []
    for word, num in shff.items():
        tasks.append(context.call_activity("Reducer_Activity_Functions", {word: num}))
    red = yield context.task_all(tasks)
    
    return [red]

main = df.Orchestrator.create(orchestrator_function)