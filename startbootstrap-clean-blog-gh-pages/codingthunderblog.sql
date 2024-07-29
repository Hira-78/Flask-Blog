-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 29, 2024 at 04:59 PM
-- Server version: 10.1.9-MariaDB
-- PHP Version: 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunderblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email_id` varchar(30) NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `mesg` varchar(200) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email_id`, `phone_num`, `mesg`, `date`) VALUES
(1, 'Hira', 'hirafareed.8888@gmail.com', '03040553497', 'Hello, its Hira here, how are you?\r\n', '2024-07-27 13:24:56'),
(8, 'Hira', 'hirafareed.8888@gmail.com', '03040553497', 'its hira', '2024-07-27 16:16:37');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `tagline` varchar(100) NOT NULL,
  `slug` varchar(30) NOT NULL,
  `content` varchar(500) NOT NULL,
  `img_file` varchar(50) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'Lets Learn about Computer programming...', 'What is computer programming?', 'Technology-Programming', 'Computer programming or coding is the composition of sequences of instructions, called programs, that computers can follow to perform tasks. It involves designing and implementing algorithms, step-by-step specifications of procedures, by writing code in one or more programming languages. Programmers typically use high-level programming languages that are more easily intelligible to humans than machine code, which is directly executed by the central processing unit. ', 'sample-post-image.jpg', '2024-07-28 21:15:37'),
(3, 'New to C++ Programming?', 'What is C++?(And how to learn it)', 'tech-programming', 'C++ (or “C-plus-plus”) is a generic programming language for building software. It''s an object-oriented language. In other words, it emphasizes using data fields with unique attributes (a.k.a. objects) rather than logic or functions. A common example of an object is a user account on a website.', 'post-sample-image.jpg', '2024-07-27 18:49:12'),
(4, 'Website Building', 'The Beginner''s Guide to Website Development', 'tech-web-dev', 'Web development refers to the overall process of creating websites or web applications, including the project''s design, layout, coding, content creation, and functionality. It involves using a combination of programming languages, tools, and frameworks to bring a website or web application to life.', 'post-sample-image.jpg', '2024-07-27 18:50:08'),
(6, 'What is Golang?', 'Go, also known as Golang, is an open-source, compiled, and statically typed programming language des', 'tech-programming-languages', 'Go, also called Golang or Go language, is an Open Source programming language that Google developed. Software developers use Go in an array of operating systems and frameworks to develop web applications, cloud and networking services, and other types of software.\r\n\r\nGo is statically typed, explicit and modeled after the C programming language. Because of Go language''s fast startup time, low runtime overhead and ability to run without a virtual machine (VM), it has become a very popular language', 'post-sample-image.jpg', '2024-07-28 20:57:50'),
(7, 'What is Golang?', 'Go, also known as Golang, is an open-source, compiled, and statically typed programming language des', 'tech-programming-languages', 'Go, also called Golang or Go language, is an Open Source programming language that Google developed. Software developers use Go in an array of operating systems and frameworks to develop web applications, cloud and networking services, and other types of software.\r\n\r\nGo is statically typed, explicit and modeled after the C programming language. Because of Go language''s fast startup time, low runtime overhead and ability to run without a virtual machine (VM), it has become a very popular language', 'post-sample-image.jpg', '2024-07-28 21:08:54');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
