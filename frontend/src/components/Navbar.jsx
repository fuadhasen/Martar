import { Link } from 'react-router-dom';
const Navbar = () => {
    return (
        <nav className="bg-amber-50 shadow-md">
            <div className="container mx-auto px-6 py-4 flex justify-between items-center">
                <h1 className="text-2xl font-bold text-amber-600"><span className="font-handy text-3xl uppercase">matar</span></h1>
                <div>
                    <Link to="/login" className="text-gray-600 hover:text-amber-600 px-4">Login</Link>
                    <Link to="/register" className="bg-amber-600 text-white px-4 py-2 rounded-md hover:bg-amber-700">Sign Up</Link>
                </div>
            </div>
        </nav>
    );
};
export default Navbar;
