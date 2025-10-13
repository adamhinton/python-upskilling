// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/description/


// Given the array restaurants where  restaurants[i] = [idi, ratingi, 
// veganFriendlyi, pricei, distancei]. You have to filter the restaurants using three filters.

// The veganFriendly filter will be either true 
// (meaning you should only include restaurants with veganFriendlyi set to true) 
// or false (meaning you can include any restaurant). 
// In addition, you have the filters maxPrice and maxDistance 
// which are the maximum value for price and distance of restaurants you should consider respectively.

// Return the array of restaurant IDs after filtering, 
// ordered by rating from highest to lowest. 
// For restaurants with the same rating, order them by id from highest to lowest. 
// For simplicity veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.

type Restaurant = [id: number, rating: number, veganFriendly: 0 | 1, price: number, distance: number]

// Plan:
// Write isValidRestaurant helper function for filtering

// Filter restaurants array to get rid of invalid restaurants
// Sort that array:
    // First by rating
    // Then by id if ratings are equal

// Make an array of the restaurant ids in order
// Return array of ids

function filterRestaurants(restaurants: Restaurant[], veganFriendly: 0 | 1, maxPrice: number, maxDistance: number): number[] {
    
    const validSortedRestaurantIDs = restaurants.filter((restaurant) => isValidRestaurant(restaurant, veganFriendly, maxPrice, maxDistance))
    .sort((restA, restB) =>{
        const restAID = restA[0]
        const restBID = restB[0]

        const restARating = restA[1]
        const restBRating = restB[1]

        if (restARating !== restBRating) {
            // Descending order by rating
            return restBRating - restARating
        }

        else{
            // Descending order by id
           return restBID - restAID 
        }
    })
    .map(restaurant => restaurant[0])

    return validSortedRestaurantIDs
};


const isValidRestaurant = (restaurant: Restaurant, shouldBeVeganFriendly: 0 | 1, maxPrice: number, maxDistance: number): boolean => {
        const [, , veganFriendly, price, distance] = restaurant;

        const isValidVeganFriendly = shouldBeVeganFriendly === 0 || (veganFriendly === 1)
        const isValidPrice = price <= maxPrice
        const isValidDistance = distance <= maxDistance

        return isValidVeganFriendly && isValidPrice && isValidDistance
    }


// console.log(filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 1, 50, 10)) // 
console.log(filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 1, 50, 10)) // [3, 1, 5]