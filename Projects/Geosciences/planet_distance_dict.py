# dictionary distances of the planets from the Sun
def run():
    planet_distance ={
        'Mercury' : '57 900 km x 1000',
        'Venus' : '108 200 km x 1000',
        'Earth' : '149 598 km x 1000',
        'Mars' : '230 000 km x 1000',
        'Jupiter' : '779 000 km x 1000',
        'Saturn' : '1 427 000 km x 1000',
        'Uranus' : '2 869 000 km x 1000',
        'Neptune' : '4 498 000 km x 1000'
    }
    for planet, distance in planet_distance.items():
        print('The planet ' + planet + ' has ' + distance + ' distance from the Sun' )


if __name__ == '__main__':
    run()