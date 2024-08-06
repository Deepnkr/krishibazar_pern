import React from 'react'

const SignupScreen = () => {
  return (
   <>
   <div className="bg-grey-lighter min-h-screen flex flex-col">
    <div className="container max-w-sm mx-auto flex-1 flex flex-col items-center justify-center px-2">
        <div className="bg-white px-6 py-8 rounded shadow-md text-black w-full">
            <h1 className="mb-8 text-3xl text-center">Sign up</h1>
            <form action="/signup" method="post">
                <input 
                type="text"
                className="block border border-grey-light w-full p-3 rounded mb-4"
                name="fullname"
                placeholder="Full Name" />

            <input 
                type="text"
                className="block border border-grey-light w-full p-3 rounded mb-4"
                name="email"
                placeholder="Email" />

            <input 
                type="password"
                className="block border border-grey-light w-full p-3 rounded mb-4"
                name="password"
                placeholder="Password" />
            <input 
                type="password"
                className="block border border-grey-light w-full p-3 rounded mb-4"
                name="cpassword"
                placeholder="Confirm Password" />

            <button
                type="submit"
                className="w-full text-center py-3 rounded bg-green-600 text-white hover:bg-green-dark "
            >Create Account</button>

            <div className="text-center text-sm text-grey-dark mt-4">
                By signing up, you agree to the 
                <a className="no-underline border-b border-grey-dark text-grey-dark" href="#">
                    Terms of Service
                </a> and 
                <a className="no-underline border-b border-grey-dark text-grey-dark" href="#">
                    Privacy Policy
                </a>
            </div>
            </form>
            
        </div>

        <p className="text-sm text-center text-green-600">Already have an account! <a href="login" className="text-indigo-400 focus:outline-none focus:underline focus:text-green-600 dark:focus:border-indigo-800">Sign In</a>.</p>
    </div>
</div>
   </>
  )
}

export default SignupScreen