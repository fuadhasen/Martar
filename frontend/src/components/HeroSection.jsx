const HeroSection = () => {
    return (
        <section className="bg-blue-600 text-white py-20">
            <div className="container mx-auto text-center">
                <h1 className="text-4xl font-bold">Explore Morocco with Ease</h1>
                <p className="mt-4 text-lg">Find trusted transport options to make your journey memorable.</p>
                <div className="mt-6">
                    <a href="/trips" className="bg-white text-blue-600 px-6 py-3 rounded-md shadow-md hover:bg-gray-100">Find a Trip</a>
                    <a href="/driver/register" className="ml-4 bg-blue-700 text-white px-6 py-3 rounded-md shadow-md hover:bg-blue-800">Become a Driver</a>
                </div>
            </div>
        </section>
    );
};
export default HeroSection;