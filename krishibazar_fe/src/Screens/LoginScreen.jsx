import React from 'react'

const LoginScreen = () => {
  return (
    <>
    <div className="flex items-center min-h-screen bg-white ">
    <div className="container mx-auto">
        <div className="max-w-md mx-auto my-10">
            <div className="text-center">
                <h1 className="my-3 text-3xl font-semibold text-black ">Sign in</h1>
                <p className="text-gray-500 dark:text-gray-400">Sign in to access your account</p>
            </div>
            <div className="m-7">
                <form action="/login" method="post">
                    <div className="mb-6">
                        <label for="email" className="block mb-2 text-sm text-black">Email Address</label>
                        <input type="email" name="email" id="email" placeholder="you@company.com" className="w-full px-3 py-2 placeholder-gray-400 border border-black rounded-md " />
                    </div>
                    <div className="mb-6">
                        <div className="flex justify-between mb-2">
                            <label for="password" className="text-sm text-black">Password</label>
                            <a href="#!" className="text-sm text-black">Forgot password?</a>
                        </div>
                        <input type="password" name="password" id="password" placeholder="Your Password" className="w-full px-3 py-2 placeholder-gray-400 border border-black rounded-md" />
                    </div>
                    <div className="mb-6">
                        <button type="submit" className="w-full px-3 py-4 text-white bg-green-600 rounded-md focus:bg-indigo-600 focus:outline-none">Sign in</button>
                    </div>
                    <p className="text-sm text-center text-green-600">Don&#x27;t have an account yet? <a href="signup" className="text-indigo-400 focus:outline-none focus:underline focus:text-indigo-500 dark:focus:border-indigo-800">Sign up</a>.</p>
                </form>
            </div>
        </div>
    </div>
</div>
    </>
  )
}

export default LoginScreen