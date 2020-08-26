# def bus_stopage_list():
dict = {
    0: 'Abdullahpur', 1: 'Adabor', 2: 'Adamjee College', 3: 'Agargaon', 4: 'Airport', 5: 'Aminbazar',
    6: 'Ansar Camp', 7: 'Arambagh', 8: 'Asad Gate', 9: 'Ashulia Bazar', 10: 'Azampur', 11: 'Azimpur',
    12: 'Babu Bazar', 13: 'Badda', 14: 'Baipayl', 15: 'Balughat', 16: 'Kakoli', 17: 'Banani', 18: 'Banasree',
    19: 'Bangla College', 20: 'Bangla Motor', 21: 'Basabo', 22: 'Bashtola', 23: 'Bashundhara', 24: 'Bijoy Sarani',
    25: 'Bosila', 26: 'CMH', 27: 'Chairman Bari', 28: 'Chashara', 29: 'Chiriakhana', 30: 'City College',
    31: 'College Gate', 32: 'Darussalam', 33: 'Daynik Bangla Mor', 34: 'Demra', 35: 'Dhanmondi 27',
    36: 'Dhanmondi 32', 37: 'Dhour', 38: 'Diabari', 39: 'Duaripara', 40: 'ECB Chottor', 41: 'Fantasy Kingdom',
    42: 'Farmgate', 43: 'Fulbaria', 44: 'GPO', 45: 'Gabtoli', 46: 'Garrison', 47: 'Gazipur Chowrasta',
    48: 'Golap Shah Mazar', 49: 'Gulistan', 50: 'Gulshan 1', 51: 'Gulshan 2', 52: 'Gulshan Bridge',
    53: 'Hemayetpur', 54: 'High Court', 55: 'House Building', 56: 'Ittefaq', 57: 'Jahangir Gate', 58: 'Ittefaq',
    59: 'Jamgora', 60: 'Jamuna Future Park', 61: 'Japan Garden City', 62: 'Jasimuddin', 63: 'Jatrabari',
    64: 'Jonopath Mor', 65: 'Kakoli', 66: 'Kakrail', 67: 'Kalabagan', 68: 'Kallyanpur', 69: 'Kalshi',
    70: 'Kamalapur', 71: 'Kamarpara', 72: 'Kataban', 73: 'Kawran Bazar', 74: 'Kazipara', 75: 'Keraniganj',
    76: 'Khamarbari', 77: 'Khilgaon', 78: 'Khilkhet', 79: 'Kodomtoli', 80: 'Kuril Bishwa Road', 81: 'Link Road',
    82: 'MES', 83: 'Madhya Badda', 84: 'Malibagh Mor', 85: 'Malibagh Railgate', 86: 'Manik Nagar',
    87: 'Motsho Bhaban', 88: 'Matuail', 90: 'Merul', 91: 'Mirpur 1', 92: 'Mirpur 10',
    93: 'Mirpur 11', 94: 'Mirpur 12', 95: 'Mirpur 14', 96: 'Mirpur 2', 97: 'Mirpur DOHS', 98: 'Moghbazar',
    99: 'Mohakhali', 100: 'Mohammadpur', 101: 'Motijheel', 102: 'Motsho Bhaban', 103: 'Mouchak', 104: 'Mugdapara',
    105: 'Nabisco', 106: 'Nadda', 107: 'Nandan Park', 108: 'Natun Bazar', 109: 'Naya Bazar', 110: 'New Market',
    111: 'Nilkhet', 112: 'Pallabi', 113: 'Paltan', 114: 'Police Plaza', 115: 'Press Club', 116: 'Proshika Mor',
    117: 'Purobi', 118: 'Rajarbagh', 119: 'Rajlakshmi', 120: 'Rampura', 121: 'Rampura Bridge',
    122: 'Ray Shaheb Bazar', 123: 'Rampura', 124: 'Rampura Bridge', 125: 'Rayerbag', 126: 'Rupnagar',
    127: 'Sadarghat', 128: 'Satrasta', 129: 'Savar', 130: 'Sayedabad', 131: 'Science Lab', 132: 'Shahbagh',
    133: 'Shahzadpur', 134: 'Shantinagar', 135: 'Sheora', 136: 'Shewrapara', 137: 'Shia Masjid', 138: 'Shishu Mela',
    139: 'Shonir Akhra', 140: 'Shyamoli', 141: 'Signal', 142: 'Sony Hall', 143: 'Staff Quarter', 144: 'Staff Road',
    145: 'Station Road', 146: 'TT Para', 147: 'Taltola', 148: 'Technical', 149: 'Tongi', 150: 'Uttar Badda',
    151: 'Wireless Mor', 152: 'Workshop', 153: 'Zirabo',
}
# return dict
new = {}
i = 0
while i < 153:
    if i > 88:
        new[i] = dict[i + 1]
        i += 1
    else:
        new[i] = dict[i]
        i += 1
print(dict)
print(new)
