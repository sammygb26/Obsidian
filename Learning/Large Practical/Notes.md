# Notes
PizzaDronz app controls a drone given orders.

- Delivered to top of Appleton tower
- Operates all day
- Don't need to avoid buildings
- Seagulls?
- Need to avoid **no-fly zones**
- Only one drone is available
- Drone cannot carry more than one order (4 pizza max)
- Drone can only fly for a limited amount of time before it needs recharged
- Data hosted by *REST-service*
- Solution must be data driven (not hard coded)
- **Distance tolerance** is 0.00015 degrees
---

### Drone Movement
- Drone can make at most 2000 moves before it runs out of battery
- The moves are either *fly* or *hover*
- *Flying* changes latitude and longitude by 0.00015deg (distance) in one of the 16 major compass directions (0 means east, 90 north, 180 west, 270 south)
- *Flying* moves the drone at a constant speed and with a constant rate of power consumption
- The angle is *null* when the drone is hovering
- When collecting and delivering pizzas the drone must hover 1 move
- Drone always starts at (−3.186874, 55.944494) and must finish near here to recharge
- Once the drone has entered the *central* area it cannot leave it again until its pizzas have been delivered
---

### Static Files
All these files are for testing and not for the actual program to use

- all.geojson
- bounding-box.geojson
- no-fly-zones.geojson
- restaurants.geojson
---

### REST Endpoints

- test
- centralArea
- noFlyZones
- restaurants
- orders
- orders/YYYY-MM-DD
---
### Order Makeup
- orders made from 2023-01-01 to 2023-05-31
- orders will never be larger that what the drone can carry
- minimum 1 pizza
- maximum 4 pizzas
- every order has fixed delivery charge of £1
- pizzas at most 14" in diameter
- need to *validate orders*
- need to check card number, expiration, order date, and items
- create Java object (**Order**) for this with matching JSON types
![[Pasted image 20220928152736.png]]
---
### Order Outcome
![[Pasted image 20220928152954.png]]
This defines the possible outcomes for a **Order**.

---
### Viability of Service
Need to prioritize average number of pizza orders delivered by service before battery is exhausted.

---
### Files to be Created
All files will have the date format YYYY-MM-DD appended on end for the corresponding day it is generated for. The formal is always *xxxx-YYYY-MM-DD*.

![[Pasted image 20220928153706.png]]

Final program should be called as

![[Pasted image 20220928153746.png]]

So argument 1 is the date, 2 is the website and 3 is the seed for the random number generator if used.

##### deliveries-YYY-MM-DD.json
In this file there is an array of JSON records each with the following attributes.

![[Pasted image 20220928154004.png]]

##### flightpath-YYYY-MM-DD.json
In this file there is an array of JSON records with the attributes for a move:

![[Pasted image 20220928154116.png]]

##### drone-YYY-MM-DD.geojson
This file should contain a **FeatureCollection** consisting of one Feature. This feature is a *LineString* containing a list of coordinates giving the flight math of the drone.