dic = {
    'Alabama' : {'Capital': 'Montgomery', 'Population': '4,918,689', 'State Flower': 'Camellia'},
    'California' : {'Capital': 'Sacramento', 'Population': '39,562,858', 'State Flower': 'California Poppy'},
    'Alaska' : {'Capital': 'Juneau', 'Population': '   727,951', 'State Flower': 'Forget Me Not'},
    'Arizona' : {'Capital': 'Phoenix', 'Population': '7,399,410', 'State Flower': 'Saguaro Cactus Blossom'},
    'Arkansas' : {'Capital': 'Little Rock', 'Population': '3,025,875', 'State Flower': 'Apple Blossom'},
    'Colorado' : {'Capital': 'Denver:', 'Population': '5,826,185', 'State Flower': 'White and Lavender Columbine'},
    'Connecticut' : {'Capital': 'Hartford', 'Population': '3,559,054', 'State Flower': 'Mountain Laurel'},
    'Delaware' : {'Capital': 'Dover', 'Population': '982,049', 'State Flower': 'Peach Blossom'},
    'Florida' : {'Capital': 'Tallahassee', 'Population': '21,711,157', 'State Flower': 'Orange Blossom'},
    'Georgia' : {'Capital': 'Atlanta', 'Population': '10,723,715', 'State Flower': 'Cherokee Rose'},
    'Hawaii' : {'Capital': 'Honolulu', 'Population': '1,411,151', 'State Flower': 'Hibiscus'},
    'Idaho' : {'Capital': 'Boise', 'Population': '1,823,594', 'State Flower': 'Syringa'},
    'Illinois' : {'Capital': 'Springfield', 'Population': '12,620,571l', 'State Flower': 'Purple Violet'},
    'Indiana' : {'Capital': 'Indianapolis', 'Population': '6,768,941', 'State Flower': 'Peony'},
    'Iowa' : {'Capital': 'Des Moines', 'Population': '3,161,522', 'State Flower': 'Wild Prairie Rose'},
    'Kansas' : {'Capital': 'Topeka', 'Population': '2,915,269', 'State Flower': 'Sunflower'},
    'Kentucky' : {'Capital': 'Frankfort', 'Population': '4,474,193', 'State Flower': 'Goldenrod'},
    'Louisiana' : {'Capital': 'Baton Rouge', 'Population': '4,637,898', 'State Flower': 'Magnolia'},
    'Maine' : {'Capital': 'Augusta', 'Population': '1,349,367', 'State Flower': 'White Pine Cone and Tassel'},
    'Maryland' : {'Capital': 'Annapolis', 'Population': '6,055,558', 'State Flower': 'Black-Eyed Susan'},
    'Massachusetts' : {'Capital': 'Boston', 'Population': '6,902,371', 'State Flower': 'Mayflower'},
    'Michigan' : {'Capital': 'Lansing', 'Population': '9,989,642', 'State Flower': 'Apple Blossom'},
    'Minnesota' : {'Capital': 'Saint Paul', 'Population': '5,673,015', 'State Flower': 'Pink and White Lady Slipper'},
    'Mississippi' : {'Capital': 'Jackson', 'Population': '2,971,278', 'State Flower': 'Magnolia'},
    'Missouri' : {'Capital': 'Jefferson City', 'Population': '6,153,233', 'State Flower': 'White Hawthorn Blossom'},
    'Montana' : {'Capital': 'Helena', 'Population': '1,076,891', 'State Flower': 'Bitterroot'},
    'Nebraska' : {'Capital': 'Lincoln', 'Population': '1,943,202', 'State Flower': 'Goldenrod'},
    'Nevada' : {'Capital': 'Carson City', 'Population': '3,132,971', 'State Flower': 'Sagebrush'},
    'New Hampshire' : {'Capital': 'Concord', 'Population': '1,365,957', 'State Flower': 'Purple Lilac'},
    'New Jersey' : {'Capital': 'Trenton', 'Population': '8,878,355', 'State Flower': 'Violet'},
    'New Mexico' : {'Capital': 'Santa Fe', 'Population': '2,100,917', 'State Flower': 'Yucca Flower'},
    'New York' : {'Capital': 'Albany', 'Population': '19,376,771', 'State Flower': 'Rose'},
    'North Carolina' : {'Capital': 'Raleigh', 'Population': '10,594,553', 'State Flower': 'Dogwood'},
    'Ohio' : {'Capital': 'Columbus', 'Population': '11,701,859', 'State Flower': 'Scarlet Carnation'},
    'Oklahoma' : {'Capital': 'Oklahoma City', 'Population': '3,973,707', 'State Flower': 'Mistletoe'},
    'Oregon' : {'Capital': 'Salem', 'Population': '4,253,588', 'State Flower': 'Oregon Grape'},
    'Pennsylvania' : {'Capital': 'Harrisburg', 'Population': '12,803,056', 'State Flower': 'Mountain Laurel'},
    'Rhode Island' : {'Capital': 'Providence', 'Population': '1,060,435', 'State Flower': 'Violet'},
    'South Carolina' : {'Capital': 'Columbia', 'Population': '5,213,272', 'State Flower': 'Yellow Jessamine'},
    'North Dakota' : {'Capital': 'Bismarck', 'Population': '766,044', 'State Flower': 'Wild Prairie Rose'},
    'South Dakota' : {'Capital': 'Pierre', 'Population': '890,620', 'State Flower': 'Pasque Flower'},
    'Tennessee' : {'Capital': 'Nashville', 'Population': '6,886,717', 'State Flower': 'Iris'},
    'Texas' : {'Capital': 'Austin', 'Population': '29,363,096', 'State Flower': 'Bluebonnet'},
    'Utah' : {'Capital': 'Salt Lake City', 'Population': '3,258,366', 'State Flower': 'Sego Lily'},
    'Vermont' : {'Capital': 'Montpelier', 'Population': '623,620', 'State Flower': 'Red Clover'},
    'Virginia' : {'Capital': 'Richmond', 'Population': '8,569,752', 'State Flower': 'Dogwood'},
    'Washington' : {'Capital': 'Olympia', 'Population': '7,705,917', 'State Flower': 'Pink Rhododendron'},
    'West Virginia' : {'Capital': 'Charleston', 'Population': '1,780,003', 'State Flower': 'Rhododendron'},
    'Wisconsin' : {'Capital': 'Madison', 'Population': '5,837,462', 'State Flower': 'Wood Violet'},
    'Wyoming' : {'Capital': 'Cheyenne', 'Population': '579,917', 'State Flower': 'Indian Paintbrush'}
}


def edit_pop():
    user = str(input("Enter a state: "))
    dictionary = dic
    state_search = dictionary[user]
    state_pop = state_search['Population']
    print("Current population:", state_pop, "\n")
    
    # Changing the value of a state
    newPopulation = str(input("Enter the new population for the state: "))
    
    #There are two ways you can change the value, both below work. I however prefer the second one
    
    #first method
    # dictionary = {**dictionary, user: newPopulation} #changes the value through unpacking the dictionary
    # print(dictionary[user]) #prints the new population of the state given when searching
    
    #second method
    dictionary[user] = newPopulation #this is a simpler method of changing the value compared to the one above.
    print("New population for ", user, ":", dictionary[user])  #prints the new population of the state given when searching
    
#here am running the function edit_pop()
edit_pop()