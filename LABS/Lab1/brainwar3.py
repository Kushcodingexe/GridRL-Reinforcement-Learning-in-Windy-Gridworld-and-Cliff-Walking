from graphviz import Digraph

# Create a Digraph object with left-to-right layout for presentation style
dot = Digraph(comment='Cost Calculation Flowchart', format='png')
dot.attr(rankdir='LR', size='8,5')

# Set global node attributes
dot.attr('node', shape='box', style='filled,rounded', fontname='Calibri', fontsize='11', fontcolor='black')

# Define nodes with custom fillcolors for a vibrant look
dot.node('A', 'Start: Input 50,000 Cars (2027)', fillcolor='lightyellow')
dot.node('B', 'Gather Base Cost Data:\n• Direct Material\n• Factory Labor\n• HR & Admin\n• Logistics\n• S&M\n• CAPEX & Depreciation', fillcolor='lightblue')
dot.node('C', 'Calculate Production Cost per Car\n(Material + Labor + HR & Admin)', fillcolor='palegreen')
dot.node('D', 'Calculate Total Production Cost\n(Production Cost × 50,000)', fillcolor='lightpink')
dot.node('E', 'Determine Inventory Requirements\n(10-day Safety Stock + Cycle Stock)', fillcolor='wheat')
dot.node('F', 'Compute Inventory Value\n(Average Inventory × Production Cost per Car)', fillcolor='thistle')
dot.node('G', 'Apply Holding Rate\n(Calculate Inventory Carrying Cost)', fillcolor='powderblue')
dot.node('H', 'Compute Logistics Cost\n(Per Car Cost × 50,000)', fillcolor='lightcoral')
dot.node('I', 'Add S&M and Depreciation Costs', fillcolor='lightgray')
dot.node('J', 'Sum All Components for Total Cost', fillcolor='lightsalmon')
dot.node('K', 'Apply Synergy Discounts (if applicable):\n• Raw Material\n• Factory Labor\n• Logistics', fillcolor='khaki')
dot.node('L', 'Compare Total Costs Across Locations', fillcolor='plum')
dot.node('M', 'Select Optimal Location', fillcolor='palegoldenrod')

# Define edges to show the flow
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H')
dot.edge('H', 'I')
dot.edge('I', 'J')
dot.edge('J', 'K')
dot.edge('K', 'L')
dot.edge('L', 'M')

# Render the flowchart image and save it as a PNG file (suitable for PowerPoint)
dot.render('colorful_cost_flowchart', view=True)
