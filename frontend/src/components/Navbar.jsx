const Navbar = () => {
    return (
        <nav className="bg-white shadow-md">
            <div className="container mx-auto px-6 py-4 flex justify-between items-center">
                <h1 className="text-2xl font-bold text-blue-600">Tourist Transport</h1>
                <div>
                    <a href="/login" className="text-gray-600 hover:text-blue-600 px-4">Login</a>
                    <a href="/register" className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Sign Up</a>
                </div>
            </div>
        </nav>
    );
};
export default Navbar;
