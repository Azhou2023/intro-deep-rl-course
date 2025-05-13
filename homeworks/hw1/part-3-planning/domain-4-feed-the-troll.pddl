
(define (domain action-castle)
   (:requirements :strips :typing)
   (:types player monster location direction monster item fishingpole food)

   (:action go
      :parameters (?dir - direction ?p - player ?l1 - location ?l2 - location)
      :precondition (and (at ?p ?l1) (connected ?l1 ?dir ?l2) (not (blocked ?l1 ?dir ?l2)))
      :effect (and (at ?p ?l2) (not (at ?p ?l1)))
   )

   (:action get
      :parameters (?i - item ?p - player ?l - location)
      :precondition (and (at ?i ?l) (at ?p ?l))
      :effect (and (not (at ?i ?l)) (inventory ?p ?i))
   )

   (:action drop
      :parameters (?i - item ?p - player ?l - location)
      :precondition (and (inventory ?p ?i) (at ?p ?l))
      :effect (and (at ?i ?l) (not (inventory ?p ?i)))
   )

   (:action gofish
      :parameters (?pole - fishingpole ?p - player ?l - location ?fish - food)
      :precondition (and (at ?p ?l) (haslake ?l) (inventory ?p ?pole))
      :effect (and (at ?fish ?l))
   )

   (:action feed
      :parameters (?p - player ?m - monster ?l - location ?f - food)
      :precondition (and (inventory ?p ?f) (hungry ?m) (at ?p ?l) (at ?m ?l))
      :effect (and (not (inventory ?p ?f)) (not (hungry ?m)))
   )
)
