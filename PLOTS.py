import matplotlib.pyplot as plt
from datetime import datetime

def occupancy_1D(figure, ax, ch, entries, title, xlabel, ylabel, xticks=[0, 8, 16, 24, 32, 40, 48, 56, 63]):
    """    
    The function plots the histogram of the occupancy of 64 channels (1 MiniDT chamber) 
    
    ----------          
    Parameters
    ----------
    figure: Figure
        Figure in which the subplots are drawn
        
    ax : AxesSubplot
        Axes of the subplot in which the function draws
          
    ch : array-like
         X bins of the bar plot
    
    entr : array-like
        Height of the bars
    
    title : string
        Title of the plot
    
    xlabel : string
        Label of x axis
    
    ylabel : string
        Label of y axis
        
    xticks : list
        Labels of x axis ticks
        
    """
       
    ax.cla()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(xticks)
    ax.bar(ch,entries, width =1, color = '#1f77b4')
    ax.set_title(datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    plt.pause(.0001)
    plt.show()
    extent = ax.get_window_extent().transformed(figure.dpi_scale_trans.inverted())
    figure.savefig(title+'.PNG', bbox_inches=extent.expanded(1.1, 1.25))

    
def occupancy_2D(figure, ax, entries, title, xlabel, ylabel):
    """    
    The function plots the 2D occupancy of 64 channels (1 MiniDT chamber) 
    
    ----------          
    Parameters
    ----------
    figure: Figure
        Figure in which the subplots are drawn
        
    ax : AxesSubplot
        Axes of the subplot in which the function draws
    
    entries : array-like
        Height of the bars
    
    title : string
        Title of the plot
    
    xlabel : string
        Label of x axis
    
    ylabel : string
        Label of y axis
        
    """

    ax.cla()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) 
    ax.set_yticks([1, 2, 3, 4])
    ax.pcolormesh(entries) 
    #plt.colorbar(m, ax = ax)
    ax.set_title(datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    plt.pause(.0001)
    plt.show()
    extent = ax.get_window_extent().transformed(figure.dpi_scale_trans.inverted())
    figure.savefig(title+'.PNG', bbox_inches=extent.expanded(1.1, 1.2))