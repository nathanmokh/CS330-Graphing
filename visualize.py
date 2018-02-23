import matplotlib.pyplot as plt
def visualizeAverages(averages):
    """Takes a list of averages and outputs chart"""
    y = averages
    x = [16,32,64,128,256,512,1024,2048,4096,8192]
    xPlot = range(len(y))
    plt.plot(xPlot,y)
    plt.xticks(xPlot,x)
    plt.ylabel('Average Weight')
    plt.xlabel('Values of n')
    plt.title('Average Weight Growth as n Increases')
    
