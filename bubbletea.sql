SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



CREATE TABLE `cart` (
  `id` int(11) NOT NULL,
  `content` int(11) DEFAULT NULL,
  `PRICE` int(11) DEFAULT NULL,
  `date_of_order` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



CREATE TABLE `extras` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `produit` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `prix` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `extras` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `image` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `prenom` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `pays` varchar(255) DEFAULT NULL,
  `ville` varchar(255) DEFAULT NULL,
  `code_postal` varchar(5) DEFAULT NULL,
  `nombre_achat` int(11) DEFAULT NULL,
  `mdp` varchar(255) DEFAULT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `content_id` (`content`);

ALTER TABLE `extras`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `cart_id` (`produit`);


ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `extra_id` (`extras`);

ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`);


ALTER TABLE `cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `extras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `cart`
  ADD CONSTRAINT `content_id` FOREIGN KEY (`content`) REFERENCES `products` (`id`);


ALTER TABLE `orders`
  ADD CONSTRAINT `cart_id` FOREIGN KEY (`produit`) REFERENCES `cart` (`id`),
  ADD CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);


ALTER TABLE `products`
  ADD CONSTRAINT `extra_id` FOREIGN KEY (`extras`) REFERENCES `extras` (`id`);


ALTER TABLE `users`
  ADD CONSTRAINT `role_id` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

