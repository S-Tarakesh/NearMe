# Ex04 Places Around Me
## Date: 

## AIM
To develop a website to display details about the places around my house.

## DESIGN STEPS

### STEP 1
Create a Django admin interface.

### STEP 2
Download your city map from Google.

### STEP 3
Using ```<map>``` tag name the map.

### STEP 4
Create clickable regions in the image using ```<area>``` tag.

### STEP 5
Write HTML programs for all the regions identified.

### STEP 6
Execute the programs and publish them.

## CODE
```
map.html
<!DOCTYPE html>
<html>
<head>
    <title>My City</title>

</head>
<body>

<h1 align="center">
    <font color="blue">Paruthipattu</font>

</h1>
<h3 align="center">
    <font color="red">TARAKESH S (25012132)</font>
</h3>
<img src= 'paruthipattu.png' usemap="#nearme" align="right" ></img>
<map name="nearme">
    <area shape="rect" coords="437,386,601,422" href="Gazon_turf.html" name="Gazon_turf">    
    <area shape="rect" coords="851,155,1107,266" href="Geetha_Citadel_Wedding.html" name="Geetha_Citadel_Wedding">
    <area shape="rect" coords="836,286,924,368" href ="Government_Park.html" name="Anna Park">
    <area shape="rect" coords="1331,232,1159,193" href="Mahindra_Happinest.html" name="Mahindra Happinest">
    <area shape="circle" coords="616,315,21" href="Angalamman_Temple.html" name="Angalamman Temple">
</map>
</body>

</html>
```
```
Gazon_turf.html
<!DOCTYPE HTML>
<html>
<head>
    <title>Gazon_turf</title>
<style>
    body {
        font-family: Arial, sans-serif;
        font-weight: lighter;
        background-color: lightgreen;
    }
    #line {
        width: 100%;
        height: 2px;
        background-color: black;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
</head>
<body>
<h1 align="center">
    <font color="blue">Gazon_turf</font>
</h1>
<div id="line"></div>
<h2>
GAZON the turf is a sports turf facility located in Paruthippattu (near Sriram Nagar, Avadi) in Chennai.
It's an all-weather synthetic turf ground where people can play games like football and box cricket,
and it offers basic amenities such as parking, restrooms, drinking water, CCTV, Wi-Fi, resting space, and first aid.<br> 
The venue is open 24/7 and can be booked for casual play or group matches
</h2>
<img src="Gazon_turf.png">
</body>

</html>
```
```
Geetha_Citadel_Wedding.html
<!DOCTYPE html>
<html>
<head>
    <title>Geetha_Citadel_Wedding</title>
<style>
    body {
        font-family: Arial, sans-serif;
        font-weight: lighter;
        background-color: lightyellow;
    }
    #line {
        width: 100%;
        height: 2px;
        background-color: black;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
</head>
<body>

<h1 align="center">
    <font color="blue">Geetha_Citadel_Wedding</font>
</h1>
<div id="line"></div>
<h2>
    Geetha Citadel Wedding & Conventions is a wedding and event venue in Paruthipattu, Avadi (Chennai) known for hosting weddings, receptions, and other large celebrations.<br> 
    It offers spacious indoor halls and outdoor lawn areas with capacities to accommodate several hundred guests, ample parking, and facilities like air-conditioning, guest rooms, valet/security services, and customizable event spaces.<br> 
    The venue aims to provide an elegant and functional setting for big Indian weddings and social or corporate functions at competitive rates.
</h2>
<img src="Geetha_Citadel_Wedding.png">
</body>

</html>
```
```
Government_Park.html
<DOCTYPE html>
<html>

<head>
    <title>Government_Park</title>
<style>
    body {
        font-family: Arial, sans-serif;
        font-weight: lighter;
        background-color: pink;
    }
    #line {
        width: 100%;
        height: 2px;
        background-color: black;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
</head>
<body>

<h1 align="center">
    <font color="blue">Government_Park</font>
</h1>
<div id="line"></div>
<h2>
    Government Park, also known as Anna Park, is a public recreational area located in Paruthipattu, Avadi (Chennai).<br> 
    It features well-maintained green spaces, walking paths, children's play areas, and seating arrangements for visitors to relax and enjoy nature.<br> 
    The park is a popular spot for families, fitness enthusiasts, and individuals seeking a peaceful environment away from the urban hustle.<br> 
    It often hosts community events and activities, making it a vibrant part of the local neighborhood.</h2>
<img src="Government_Park.png">
</body>
</html>
```
```
Mahindra_happinest.html
<!DOCTYPE html>
<html>
<head>
    <title>Mahindra_happinest</title>
<style>
    body {
        font-family: Arial, sans-serif;
        font-weight: lighter;
        background-color: aqua;
    }
    #line {
        width: 100%;
        height: 2px;
        background-color: black;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
</head>
<body>
<h1 align="center">
    <font color="blue">Mahindra_happinest</font>
</h1>
<div id="line"></div>
<h2>
    Mahindra Happinest in Avadi (Paruthipattu), Chennai is a residential housing project by Mahindra Lifespaces offering affordable 1 BHK and 2 BHK apartments in a gated community setting.<br> 
    It's spread over a sizeable area with landscaped open spaces and modern amenities such as a clubhouse, gym, children's play areas, and security features.
    The development is known for its green, sustainable design and good connectivity to public transport, schools, hospitals, and the nearby Ambattur IT Park, making it a popular choice for middle-income homebuyers.
</h2>
<img src="Mahindra_happinest.png">
</body>


</html>
```
```
Angalamman_Temple.html
<DOCTYPE html>
<html>
<head>
    <title>Angalamman_Temple</title>
<style>
    body {
        font-family: Arial, sans-serif;
        font-weight: lighter;
        background-color: lightblue;
    }
    #line {
        width: 100%;
        height: 2px;
        background-color: black;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
</head>
<body>
<h1 align="center">
    <font color="blue">Angalamman_Temple</font>
</h1>
<div id="line"></div>
<h2>
    Angalamman Temple is a Hindu temple located in Paruthipattu, Avadi (Chennai) dedicated to Goddess Angalamman, a fierce form of the Mother Goddess.<br> 
    The temple is known for its vibrant festivals, especially during the Tamil month of Aadi (July-August), when devotees gather in large numbers to seek blessings and participate in rituals.<br> 
    The temple architecture features traditional Dravidian style with intricate carvings and sculptures, making it a significant religious and cultural landmark in the local community.
</h2>
<img src="Angalamman_Temple.png">
</body>

</html>
```
## OUTPUT







## RESULT
The program for implementing image maps using HTML is executed successfully.
