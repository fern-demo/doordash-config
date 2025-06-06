Sur cette page

# Exigences concernant l'intégration

API: Drive

Ce document traite de l’API Drive. Si vous utilisez l’API Drive (classique), consultez les [exigences d’intégration de Drive (classique)](/fr-CA/docs/drive_classic/overview/integration_requirements).

Notre mission est simple : nous voulons être le service de livraison local le plus simple et le plus fiable qui soit, tout en protégeant les commerçants, les clients et les Dashers. Nous y parvenons grâce à un portail en libre-service qui permet aux développeurs de tirer parti du vaste réseau de Dashers de DoorDash dans leur propre entreprise, où chaque intégration est examinée par notre équipe pour s'assurer que nos normes technologiques et juridiques sont respectées.

## Avant de demander l'accès à la production[​](#avant-de-demander-laccès-à-la-production "Lien direct vers le titre")

Avant d’accorder l’accès à notre environnement de production pour vous permettre de commencer à faire des livraisons en direct, l'équipe de DoorDash examinera et approuvera votre produit fini. Pour vous assurer que ce processus se déroule sans problème, passez en revue la liste de vérification ci-dessous avant de demander un accès à la production. Notez que le fait de respecter toutes les conditions énoncées ci-dessous ne garantit pas l’accès à la production, mais c'est un excellent début.

Assurez-vous que :

* Vous avez suffisamment de mesures de restriction en place pour empêcher le ramassage ou la livraison d'articles restreints. Ces articles incluent notamment le tabac, le cannabis et d'autres drogues illicites, les armes et les explosifs. Pour obtenir plus de détails sur les articles que DoorDash ne peut pas livrer, consultez la liste complète des articles soumis à des restrictions, ci-dessous.
* Vous avez lu et accepté notre licence technologique et nos conditions d'utilisation.
* Vous avez utilisé le simulateur de livraison pour créer des tests de livraisons et vous familiariser avec le fonctionnement de DoorDash.
* Vous êtes prêt à effectuer une démonstration en direct avec l'équipe de DoorDash. Vous partagerez votre écran et nous guiderez du début à la fin d’un test pour démontrer l'expérience utilisateur complète.
* Les champs obligatoires sont transmis dans tous les appels d'API. Tous les champs obligatoires sont indiqués dans notre document de référence d'API.
* Les détails clés de la livraison, comme l'identifiant de livraison/d'assistance fourni par DoorDash sont rendus accessibles aux utilisateurs concernés dans votre interface utilisateur. Vous pouvez en savoir plus sur nos exigences minimales en matière d'interface utilisateur ci-dessous et dans notre page Comment > Obtenir un accès à la production.

## Exigences juridiques et de sécurité[​](#exigences-juridiques-et-de-sécurité "Lien direct vers le titre")

DoorDash s'engage à assurer la sûreté et la sécurité de tous les utilisateurs de sa plateforme et de ses services, y compris les Dashers, les commerçants et les clients. Notre priorité est de nous assurer que toute personne qui demande ou facilite une livraison par l'entremise de DoorDash puisse le faire en toute sécurité et en toute confiance. Nous avons énuméré les principaux points ci-dessous, mais cette liste n'est pas exhaustive. Si votre entreprise ou votre produit ne répond pas à ces exigences, l'équipe de DoorDash peut refuser votre demande d'accès à la production. Et si vous avez déjà été approuvé pour la production, nous nous réservons le droit de désactiver vos identifiants de production.

### Articles restreints[​](#articles-restreints "Lien direct vers le titre")

DoorDash restreint la vente de certains articles (y compris, mais sans s'y limiter, ceux énumérés ci-dessous) pour maintenir une expérience utilisateur de grande qualité et se conformer aux exigences légales. Il vous incombe de mettre en place suffisamment des mesures de restriction pour empêcher le ramassage ou la livraison d'articles restreints.

La liste ci-dessous fournit des exemples d'articles restreints, mais n'est pas exhaustive. DoorDash peut modifier cette liste à son entière discrétion et se réserve le droit de supprimer ou de refuser de répertorier, de transporter, d'expédier, de livrer ou de rendre disponible par le biais de son service tout article mentionné ci-dessous ou tout autre article que DoorDash juge, à sa seule discrétion, dangereux ou inapproprié.

* Personnes, faune, animaux, ou restes ou parties;
* Articles illégaux; biens volés;
* Feux d'artifice, explosifs, armes à feu, armements, munitions et leurs pièces; informations sur la façon de fabriquer de tels articles;
* Articles encourageant une activité violente ou illégale;
* Articles ou matériel pour adultes, sexuellement explicites ou obscènes;
* Tout ce qui suit qui ne fait pas l’objet d’un avenant signé avec DoorDash :
  + Alcool
  + Produits du tabac ou de vapotage
  + Médicaments contre le rhume, produits pharmaceutiques, médicaments en vente libre, vitamines, dispositifs médicaux ou suppléments
* Drogues récréatives ou accessoires de consommation de drogues, y compris, mais sans s'y limiter, le cannabis ou les produits à base de CBD, le kratom ou les inhalants, y compris l'oxyde nitreux;
* Substances toxiques et poisons
* Tout article de plus de 22 kg (50 lb);
* Tout autre article dont la livraison est interdite sans permis ou licence en vertu des lois locales applicables;
* Les matières dangereuses, y compris les déchets médicaux, ou les articles toxiques ou inflammables, à l'exception des matières qui sont :
  + (i) Autres matériaux réglementés-domestiques (ORM-D) ou (ii) expédition en quantité limitée ET un bien de consommation, ET
  + En quantité ne nécessitant pas de plaques pour marchandises dangereuses
* Argent, cartes-cadeaux, billets de loterie ou valeurs mobilières;
* Produits contrefaits;
* Viandes ou crustacés crus;
* Produits d'animaux ou d'animaux sauvages menacés d'extinction; articles fabriqués à partir de produits d'animaux ou d'animaux sauvages menacés d'extinction (y compris, sans toutefois s'y limiter, l'ivoire, les cornes de rhinocéros, le caviar d'Eurasie, la viande de brousse et le foie gras);
* Articles incitant à la haine ou faisant la promotion de groupes terroristes;
* Produits revendiquant ou encourageant des résultats médicaux particuliers;
* Tout article susceptible d'être perçu comme menaçant, obscène, harcelant, inapproprié ou violant de toute autre manière les conditions générales applicables qui régissent votre relation avec DoorDash.

### Conformité aux lois et règlements[​](#conformité-aux-lois-et-règlements "Lien direct vers le titre")

Votre entreprise, y compris les employés, agents, représentants, sous-traitants et votre produit lui-même, doit se conformer à toutes les lois et réglementations applicables, et ce dans tous les marchés où elle opère.

## Exigences techniques et d’IU[​](#exigences-techniques-et-diu "Lien direct vers le titre")

Notre objectif est d'offrir un service de livraison fluide, simple et fiable pour toutes les parties concernées. Vous êtes responsable de concevoir et de développer un excellent produit et les lignes directrices ci-dessous, relatives à l’aspect technique et à l'interface utilisateur, visent à garantir à vos clients la meilleure expérience de commande à emporter et de livraison possible. Lisez notre page Comment > Obtenir un accès à la production pour obtenir plus de détails sur le processus de démonstration et sur la façon dont l'équipe de DoorDash évaluera votre demande d'accès à la production.

### Exigences[​](#exigences "Lien direct vers le titre")

* **L’identifiant de livraison DoorDash (`support_reference`) doit être visible pour les commerçants, les exploitants de commerces et les utilisateurs qui préparent le ramassage des commandes dans votre interface utilisateur.** Cet identifiant (un nombre entier), inclus dans nos réponses d'API, est requis pour toutes les demandes d'assistance, y compris le service de soutien aux commerçants Drive (pour les questions/problèmes non techniques concernant les livraisons, comme les remboursements) et le service de soutien aux développeurs (pour les questions/problèmes techniques/de l'API concernant les livraisons).
* L'heure de ramassage doit être indiquée à l'utilisateur ou aux utilisateurs qui préparent le ramassage. Il s'agit le plus souvent du commerçant ou de l'exploitant du commerce.
* Le nom de l'entreprise où effectuer le ramassage doit être transmis dans les demandes de livraison pour tous les cas où l'adresse de ramassage est un lieu d'affaires.
* Il existe une boucle de rétroaction claire pour l'utilisateur final si DoorDash rejette le devis ou la demande de livraison. Par exemple, si DoorDash renvoie une erreur dans l'API en raison d'une adresse de dépôt non valide, l'utilisateur final doit être invité à corriger l’adresse avant de terminer le paiement.

### Recommandations[​](#recommandations "Lien direct vers le titre")

Ces suggestions ne sont pas obligatoires, mais sont fortement recommandées pour assurer une expérience de ramassage et de livraison de haute qualité.

* Transmettez des instructions claires de ramassage et de dépôt lors de la création de livraisons.
* Présentez le lien de suivi de livraison fourni par DoorDash aux commerçants et aux clients.
* Créez des fonctionnalités permettant aux administrateurs internes ou à vos clients commerçants de visualiser et de gérer les livraisons. Par exemple, si votre entreprise est une plateforme qui permet aux clients de commander des fleurs auprès de fleuristes locaux, nous vous recommandons de créer un tableau de bord que les fleuristes peuvent utiliser pour afficher les détails des livraisons en cours et passées.

[Précédent

Prix et paiement](/fr-CA/docs/drive/overview/pricing_payment)[Suivant

How to Build for Restaurants](/fr-CA/docs/drive/how_to/build_for_restaurants)

* [Avant de demander l'accès à la production](#avant-de-demander-laccès-à-la-production)
* [Exigences juridiques et de sécurité](#exigences-juridiques-et-de-sécurité)
  + [Articles restreints](#articles-restreints)
  + [Conformité aux lois et règlements](#conformité-aux-lois-et-règlements)
* [Exigences techniques et d’IU](#exigences-techniques-et-diu)
  + [Exigences](#exigences)
  + [Recommandations](#recommandations)