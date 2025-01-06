import Navbar from '../components/Navbar';
import HeroSection from '../components/HeroSection';
import FeaturesSection from '../components/FeaturesSection';
import TestimonialsSection from '../components/TestimonialsSection';
import Footer from '../components/Footer';

const Home = () => {
    return (
        <div className="bg-gray-50 min-h-screen">
            <Navbar />
            <HeroSection />
            <FeaturesSection />
            <TestimonialsSection />
            <Footer />
        </div>
    );
};
export default Home;


