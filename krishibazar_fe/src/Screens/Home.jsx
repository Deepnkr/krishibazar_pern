import React from 'react'


const Home = () => {
  return (
    <>

    <div className="container flex flex-col px-6 py-4 mx-auto space-y-6 md:h-128 md:py-16 md:flex-row md:items-center md:space-x-6 ">
    <div className="flex flex-col items-center w-full md:flex-row md:w-1/2">
        <div className="flex justify-center order-2 mt-6 md:mt-0 md:space-y-3 md:flex-col">
            <button className="w-3 h-3 mx-2 bg-green-500 rounded-full md:mx-0 focus:outline-none"></button>
        </div>

        <div className="max-w-lg md:mx-12 md:order-2">
            <h1 className="text-3xl text-black font-medium tracking-wide md:text-4xl">Different types of grains</h1>
            <p className="mt-4 text-gray-600 dark:text-gray-300">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aut quia asperiores alias vero magnam recusandae adipisci ad vitae laudantium quod rem voluptatem eos accusantium cumque.</p>
            <div className="mt-6">
                <a href="#" className="block px-3 py-2 font-semibold text-center text-white transition-colors duration-200 transform bg-green-600 rounded-md md:inline hover:bg-blue-400">Go to Store.</a>
            </div>
        </div>
    </div>

    <div className="flex items-center justify-center w-full h-96 md:w-1/2">
        <img className="object-cover w-full h-full max-w-2xl rounded-md" src="/images/nature-food-wallpaper-preview.jpg" alt="photos of grains"/>
    </div>
</div>
<div className="container flex flex-col px-6 py-4 mx-auto space-y-6 md:h-128 md:py-16 md:flex-row md:items-center md:space-x-6 ">
    <div className="flex flex-col items-center w-full md:flex-row md:w-1/2">
        <div className="flex justify-center order-2 mt-6 md:mt-0 md:space-y-3 md:flex-col">
            <button className="w-3 h-3 mx-2 bg-green-500 rounded-full md:mx-0 focus:outline-none"></button>
        </div>
        <div className="max-w-lg md:mx-12 md:order-2">
            <h1 className="text-3xl text-black font-medium tracking-wide md:text-4xl">Wheat.</h1>
            <p className="mt-4 text-gray-600 dark:text-gray-300">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aut quia asperiores alias vero magnam recusandae adipisci ad vitae laudantium quod rem voluptatem eos accusantium cumque.</p>
            <div className="mt-6">
                <a href="#" className="block px-3 py-2 font-semibold text-center text-white transition-colors duration-200 transform bg-green-600 rounded-md md:inline hover:bg-blue-400">Go to Store.</a>
            </div>
        </div>
    </div>

    <div className="flex items-center justify-center w-full h-96 md:w-1/2">
        <img className="object-cover w-full h-full max-w-2xl rounded-md" src="images/pexels-pixabay-54084.jpg" alt="photos of grains"/>
    </div>
</div>    

    </>
  )
}

export default Home