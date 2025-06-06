Sur cette page

# Foire aux questions

### Qu'est-ce que le portail des développeurs DoorDash?[​](#quest-ce-que-le-portail-des-développeurs-doordash "Lien direct vers le titre")

Le portail des développeurs est un outil conçu pour permettre aux développeurs d'explorer et d'intégrer harmonieusement l'API Drive de DoorDash. En quelques secondes seulement, vous pouvez créer un compte de développeur et commencer à effectuer des tests dans notre environnement bac à sable. Une fois que vous aurez terminé le développement, présenté une démonstration et reçu l’évaluation de l'équipe de DoorDash, vous pourrez générer des identifiants de production dans le portail et commencer à demander aux chauffeurs d'effectuer des livraisons pour votre entreprise.

### Qu'est-ce que DoorDash Drive?[​](#quest-ce-que-doordash-drive "Lien direct vers le titre")

Drive est le service de traitement des commandes en marque blanche de DoorDash, qui permet aux commerçants d'accéder à une flotte de livraison professionnelle, sans avoir à s'occuper de la logistique. Avec DoorDash Drive, vous pouvez demander un chauffeur à tout moment, suivre vos commandes, simplifier vos coûts de livraison et augmenter vos ventes. Que vous ayez besoin d'un service de livraison flexible pour les périodes de débordement ou d'un service de livraison à la demande constant, la plateforme Drive est conçue pour fonctionner avec votre entreprise.

### Quelles sont les différences entre DoorDash Drive et Marketplace de DoorDash?[​](#quelles-sont-les-différences-entre-doordash-drive-et-marketplace-de-doordash "Lien direct vers le titre")

Marketplace de DoorDash (c'est-à-dire l'application DoorDash) permet aux clients de trouver votre entreprise et de passer des commandes. DoorDash Drive vous permet d'offrir la livraison sur votre propre plateforme, comme votre propre application ou votre propre site Web. Les détails de la commande sont communiqués à DoorDash Drive par l'intermédiaire de l'API. Un Dasher s'occupera ensuite du ramassage et de la livraison pour vous.

### Dans quels pays DoorDash Drive opère-t-il?[​](#dans-quels-pays-doordash-drive-opère-t-il "Lien direct vers le titre")

Pendant cette période bêta, l'API DoorDash Drive standard n'autorise que les livraisons aux États-Unis. Si votre entreprise exerce ses activités au Canada ou en Australie, vous devrez utiliser l'API Drive (classique). Notez que Drive (classique) n'est disponible que pour un groupe limité d'utilisateurs. Veuillez nous contacter à partir de la page du service de soutien si vous avez besoin de soutien pour les livraisons CAN/AUS et que vous n'utilisez pas Drive (classique).

### Qui peut créer un compte de développeur?[​](#qui-peut-créer-un-compte-de-développeur "Lien direct vers le titre")

Toute personne possédant une adresse courriel peut s'inscrire en tant que développeur DoorDash! Notre portail de développeur est conçu pour simplifier le processus d'intégration pour tous ceux qui cherchent à utiliser la gestion des commandes de DoorDash dans leur entreprise; des marques de commerce de détail uniques aux plateformes de services aux commerçants offertes aux l'entreprise.

### Est-ce que chaque membre de mon équipe de développement doit créer son propre compte?[​](#est-ce-que-chaque-membre-de-mon-équipe-de-développement-doit-créer-son-propre-compte "Lien direct vers le titre")

Non, un seul compte de portail de développeur par entreprise est nécessaire. Dans l'avenir, nous prendrons en charge la connexion multi-utilisateurs, de sorte que chaque membre de votre équipe pourra se connecter au même compte de développeur avec sa propre adresse courriel et son propre mot de passe.

### De quoi ai-je besoin pour commencer?[​](#de-quoi-ai-je-besoin-pour-commencer "Lien direct vers le titre")

Vous n’avez besoin que de votre nom, de votre numéro de téléphone et de votre adresse courriel pour vous inscrire et effectuer un test dans notre environnement bac à sable.

### Comment puis-je savoir si je suis dans l’environnement Drive ou Drive classique? Quelle est la différence?[​](#comment-puis-je-savoir-si-je-suis-dans-lenvironnement-drive-ou-drive-classique-quelle-est-la-différence "Lien direct vers le titre")

Drive est notre offre d'API standard. Il s’agit de l’environnement par défaut pour tous les développeurs. Drive classique est l’ancienne version de notre API (1.0) et possède une référence et des points de terminaison d’API distincts. Un groupe limité d'utilisateurs alpha a été autorisé à intégrer Drive classique, car il convient mieux aux fournisseurs d'intergiciels comme les systèmes de point de vente, les plateformes de commande en ligne et d'autres entreprises de services aux commerçants qui nécessitent une assistance pour la modélisation d'entreprise et de commerce, la livraison d'alcool, etc. Si l'URL de votre tableau de bord du portail des développeurs inclut **« /Classic »**, vous avez été inscrit sur la liste d'autorisation pour la version classique. Sinon, vous développez pour Drive.

### Combien de temps faut-il pour créer une intégration avec DoorDash?[​](#combien-de-temps-faut-il-pour-créer-une-intégration-avec-doordash "Lien direct vers le titre")

Le portail des développeurs est conçu pour fournir aux développeurs des outils et des ressources pour créer une intégration en fonction de leur propre calendrier. Selon votre propre feuille de route et les besoins de votre entreprise, cela pourrait signifier 1 à 2 jours de développement ou plusieurs petites périodes intenses. Une fois que vous avez terminé le développement, notre équipe examinera votre produit fini et vous fournira une mise à jour sur l'accès à la production dans un délai de 5 à 10 jours.

### Combien coûte la livraison par l'entremise de DoorDash Drive?[​](#combien-coûte-la-livraison-par-lentremise-de-doordash-drive "Lien direct vers le titre")

Les frais pour les livraisons demandées par l'entremise de notre API Drive standard sont dynamiques en fonction de la distance entre les points de ramassage et de dépôt. Les livraisons dans un rayon de 8 km entraînent un tarif de base de 9,75 $. Pour les livraisons au-delà de 8 km, il faut additionner des frais de 0,75 $ par tranche de 1,6 km, jusqu'à un maximum de 24 km. Ce tarif tient compte du fait que les pourboires sont facultatifs.

Pour les développeurs qui s’appuient sur notre ancienne API (c.-à-d. Drive classique), DoorDash facture des frais fixes de 7 $ par livraison, plus tous les pourboires payés par l’utilisateur final. Les pourboires sont versés directement au Dasher; la fonctionnalité est exigée dans toutes les interfaces utilisateur développées avec cette API. Ce tarif suppose que DoorDash est le fournisseur de livraison exclusif pour votre entreprise ou que DoorDash a le droit de premier refus sur toutes les livraisons. Notez que Drive (classique) n'est disponible que pour un groupe limité d'utilisateurs.

### Y a-t-il des articles qui ne peuvent pas être livrés par DoorDash?[​](#y-a-t-il-des-articles-qui-ne-peuvent-pas-être-livrés-par-doordash "Lien direct vers le titre")

Oui. La liste ci-dessous contient des exemples d'articles restreints, mais n'est pas exhaustive.

* Personnes, faune, animaux, ou restes ou parties;
* Articles illégaux; biens volés;
* Feux d'artifice, explosifs, armes à feu, armements, munitions et leurs pièces; informations sur la façon de fabriquer de tels articles;
* Articles encourageant une activité violente ou illégale;
* Articles ou matériels sexuellement explicites ou obscènes pour adultes;
* Tous les produits suivants, s’ils ne font pas l’objet d’un avenant signé avec DoorDash :
  + Alcool
  + Produits du tabac ou de vapotage
  + Médicaments contre le rhume, produits pharmaceutiques, médicaments en vente libre, vitamines, dispositifs médicaux ou suppléments
  + Drogues récréatives ou accessoires de consommation de drogues, y compris, mais sans s'y limiter, le cannabis ou les produits à base de CBD, le kratom ou les inhalants, y compris l'oxyde nitreux;
* Substances toxiques et poisons
* Tout article de plus de 22 kg (50 lb);
* Tout autre article dont la livraison est interdite sans permis ou licence en vertu des lois locales applicables;
* Les matières dangereuses, y compris les déchets médicaux, ou les articles toxiques ou inflammables, à l'exception des matières qui sont :
  + (i) d'autres matériaux réglementés-domestiques (ORM-D) ou
  + (ii) assujettis à une expédition en quantité limitée ET un bien de consommation, ET
  + En quantité ne nécessitant pas de plaques pour marchandises dangereuses
* Argent, cartes-cadeaux, billets de loterie ou valeurs mobilières négociables;
* Produits contrefaits;
* Viandes ou crustacés crus;
* Produits d'animaux ou d'animaux sauvages menacés d'extinction; articles fabriqués à partir de produits d'animaux ou d'animaux sauvages menacés d'extinction (y compris, sans toutefois s'y limiter, l'ivoire, les cornes de rhinocéros, le caviar d'Eurasie et la viande de brousse);
* Articles incitant à la haine ou faisant la promotion de groupes terroristes;
* Produits revendiquant ou encourageant des résultats médicaux particuliers;
* Tout article susceptible d'être perçu comme menaçant, obscène, harcelant, inapproprié ou violant de toute autre manière les conditions générales applicables qui régissent votre relation avec DoorDash.

### Dois-je signer un contrat d’intégration à Drive?[​](#dois-je-signer-un-contrat-dintégration-à-drive "Lien direct vers le titre")

Afin de demander l'accès à la production, vous devrez lire et accepter nos conditions d'utilisation. Les conditions d'utilisation de l'API Drive standard sont disponibles [ici](https://developer.doordash.com/terms/v2/2/) et celles de Drive classique sont disponibles [ici](https://developer.doordash.com/terms/v1/1/).

### Le suivi de livraison est-il disponible?[​](#le-suivi-de-livraison-est-il-disponible "Lien direct vers le titre")

Oui, DoorDash fournit un lien de suivi pour chaque livraison que vous pouvez exposer dans votre interface utilisateur.

### Où se trouve l’UTC par rapport aux fuseaux horaires locaux?[​](#où-se-trouve-lutc-par-rapport-aux-fuseaux-horaires-locaux "Lien direct vers le titre")

Le temps universel coordonné (UTC) a 8 heures d'avance sur l'heure normale du Pacifique, 9 heures d'avance sur l'heure normale des Rocheuses, 10 heures d'avance sur l'heure normale du Centre et 11 heures d'avance sur l'heure normale de l'Est.

### Comment serai-je informé d'une interruption de service?[​](#comment-serai-je-informé-dune-interruption-de-service "Lien direct vers le titre")

Tous les incidents à l'échelle du système, ainsi que les bilans, sont signalés [ici](https://doordash.statuspage.io/). N'hésitez pas à vous abonner aux mises à jour par courriel au besoin. Pour signaler un incident ou un problème qui n'est pas répertorié sur la page de statut, vous pouvez contacter l'équipe de DoorDash à partir de la page de service de soutien du portail des développeurs.

### Avez-vous des limites de taux?[​](#avez-vous-des-limites-de-taux "Lien direct vers le titre")

La limite est fixée à environ 300 demandes dans une période de 60 secondes. Si vous prévoyez d'effectuer des tests de charge ou de résilience, veuillez contacter l'équipe de DoorDash à partir de la page de service de soutien au moins 3 jours à l'avance. Le fait de ne pas informer DoorDash des tests de charge peut entraîner la désactivation de vos identifiants dans l'API.

### DoorDash me remboursera-t-il si la livraison est en retard?[​](#doordash-me-remboursera-t-il-si-la-livraison-est-en-retard "Lien direct vers le titre")

L'équipe de service de soutien aux commerçants de DoorDash examine au cas par cas toutes les demandes de remboursement liées aux livraisons Drive. La possibilité que DoorDash rembourse ou non une livraison et le montant de ce remboursement dépend du type de problème. Vous pouvez consulter notre tableau de remboursement ici.

### Qui livre les articles par l'entremise de DoorDash?[​](#qui-livre-les-articles-par-lentremise-de-doordash "Lien direct vers le titre")

Vous pouvez en savoir plus sur les exigences concernant les Dashers [ici](https://help.doordash.com/dashers/s/article/Requirements-for-Dashing).

[Précédent

Notes de mise à jour](/fr-CA/docs/drive/overview/release_notes)[Suivant

Commencer (API)](/fr-CA/docs/drive/tutorials/get_started)

* [Qu'est-ce que le portail des développeurs DoorDash?](#quest-ce-que-le-portail-des-développeurs-doordash)
* [Qu'est-ce que DoorDash Drive?](#quest-ce-que-doordash-drive)
* [Quelles sont les différences entre DoorDash Drive et Marketplace de DoorDash?](#quelles-sont-les-différences-entre-doordash-drive-et-marketplace-de-doordash)
* [Dans quels pays DoorDash Drive opère-t-il?](#dans-quels-pays-doordash-drive-opère-t-il)
* [Qui peut créer un compte de développeur?](#qui-peut-créer-un-compte-de-développeur)
* [Est-ce que chaque membre de mon équipe de développement doit créer son propre compte?](#est-ce-que-chaque-membre-de-mon-équipe-de-développement-doit-créer-son-propre-compte)
* [De quoi ai-je besoin pour commencer?](#de-quoi-ai-je-besoin-pour-commencer)
* [Comment puis-je savoir si je suis dans l’environnement Drive ou Drive classique? Quelle est la différence?](#comment-puis-je-savoir-si-je-suis-dans-lenvironnement-drive-ou-drive-classique-quelle-est-la-différence)
* [Combien de temps faut-il pour créer une intégration avec DoorDash?](#combien-de-temps-faut-il-pour-créer-une-intégration-avec-doordash)
* [Combien coûte la livraison par l'entremise de DoorDash Drive?](#combien-coûte-la-livraison-par-lentremise-de-doordash-drive)
* [Y a-t-il des articles qui ne peuvent pas être livrés par DoorDash?](#y-a-t-il-des-articles-qui-ne-peuvent-pas-être-livrés-par-doordash)
* [Dois-je signer un contrat d’intégration à Drive?](#dois-je-signer-un-contrat-dintégration-à-drive)
* [Le suivi de livraison est-il disponible?](#le-suivi-de-livraison-est-il-disponible)
* [Où se trouve l’UTC par rapport aux fuseaux horaires locaux?](#où-se-trouve-lutc-par-rapport-aux-fuseaux-horaires-locaux)
* [Comment serai-je informé d'une interruption de service?](#comment-serai-je-informé-dune-interruption-de-service)
* [Avez-vous des limites de taux?](#avez-vous-des-limites-de-taux)
* [DoorDash me remboursera-t-il si la livraison est en retard?](#doordash-me-remboursera-t-il-si-la-livraison-est-en-retard)
* [Qui livre les articles par l'entremise de DoorDash?](#qui-livre-les-articles-par-lentremise-de-doordash)