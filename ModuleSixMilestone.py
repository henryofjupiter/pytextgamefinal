# room navigation with dictionaries
lands = {
        'Grass Lands': {'right': 'Swamp Lands'},
        'Swamp Lands': {'down': 'Jungle Lands', 'right': 'Grass Lands'},
        'Jungle Lands': {'up': 'Swamp Lands', 'left': 'The Abyss', 'right': ' Mountain Lands', 'down': 'Check Point'},
        'The Abyss': {'right': 'Jungle Lands'},
        'Mountain Lands': {'left': 'Jungle Lands', 'up': 'Desert Lands'},
        'Desert Lands': {'down': 'Mountain Lands'},
        'Check Point': {'up': 'Jungle Lands', 'right': 'Stone Lands'},
        'Stone Lands': {'right': 'Check Point'}
    }
