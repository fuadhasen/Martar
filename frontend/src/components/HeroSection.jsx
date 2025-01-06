import { Link } from 'react-router-dom';


const HeroSection = () => {
    return (
        <section
            className="bg-[url('../../public/images/bg.webp')] bg-cover bg-center text-white"
        >
            <div className="bg-black bg-opacity-50 py-20">
                <div className="container mx-auto text-center">
                    <h1 className="text-4xl font-bold">Explore Morocco with Ease</h1>
                    <p className="mt-4 text-lg">
                        Find trusted transport options to make your journey memorable.
                    </p>
                    <div className="mt-6">
                        <Link
                            to="/trips"
                            className="bg-white text-amber-600 px-6 py-3 rounded-md shadow-md hover:bg-gray-100"
                        >
                            Find a Trip
                        </Link>
                        <Link
                            to="/apply"
                            className="ml-4 bg-amber-700 text-white px-6 py-3 rounded-md shadow-md hover:bg-amber-800"
                        >
                            Become a Driver
                        </Link>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default HeroSection;
