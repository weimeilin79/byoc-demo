package org.acme;

import io.smallrye.reactive.messaging.kafka.Record;
import org.eclipse.microprofile.reactive.messaging.Incoming;
import org.jboss.logging.Logger;

import javax.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class PlantsConsumer {

    private final Logger logger = Logger.getLogger(PlantsConsumer.class);

    @Incoming("plants")
    public void receive(Record<Integer, String> signal) {
        logger.infof("Got a signal: %s - %s", signal.key(), signal.value());
    }
}
